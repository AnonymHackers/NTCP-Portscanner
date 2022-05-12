import socket
import threading
import concurrent.futures
import sys
import time

PrintOpen = False
main = False

print_lock = threading.Lock()
try:
	if sys.argv[1] == '-select':
		ip = sys.argv[2]
		handshake = socket.gethostbyname(ip)
	if sys.argv[3] == '-thread':
		how = sys.argv[4]
	try:
		if sys.argv[5] == '-print-open':
			PrintOpen = True
	except:
		if sys.argv[5] == '-with-speed':
			main = True
			speed = sys.argv[6]
			try:
				speed = float(speed)
			except:
				speed = int(speed)
		PrintOpen = False
	try:
		if sys.argv[6] == '-with-speed':
			main = True
			speed = sys.argv[7]
			try:
				speed = float(speed)
			except:
				speed = int(speed)
	except:
		pass
except:
	print("Invalid Syntax ...")
	print(" ")
	print("if you want print opened Type: \" NTCP.py -select <Target> -max <How much Ports> -print-open \"")
	print("if you want print all Type: \" NTCP.py -select <Target> -max <How much Ports> \"")
	print(" ")
	sys.exit()
print("[NTCP] [INFORMATION] Waiting for Targets")
time.sleep(3)
print(f"       [PAYLOAD] Sending payload for get recv Handshake")
time.sleep(2)
print(f"       [+] [COMPLETED] Payload is acceptet")
print(f"       [+] [STARTING] NTCP Server to scanning Target ...")
print(f"       [+] [HANDSHAKE] Hanshake Found! Handshake under the Message")
print(f"       [FOUND] Port recv Handshake: {handshake}")

print(" ")

value = input("[NTCP] Want Starting Scanning? [Y/n]: ")
if value == 'Y' or 'y':
	pass
else:
	sys.exit()
if PrintOpen == True:
	def scan(ip, port):
		scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if main == True:
			scanner.settimeout(speed)
		else:
			scanner.settimeout(0.6)
		try:
			scanner.connect((ip, port))
			scanner.close()
			with print_lock:
				print(f"[+] [OPENED] Port [{port}] is open scanned by NTCP")
		except:
			pass

	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		for port in range(int(how)):
			executor.submit(scan, ip, port + 1)
elif PrintOpen == False:
	def scan(ip, port):
		scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		scanner.settimeout(0.1)
		try:
			scanner.connect((ip, port))
			scanner.close()
			with print_lock:
				print(f"[+] [OPENED] Port [{port}] is open scanned by NTCP")
		except:
			print(f"[+] [CLOSED] Port [{port}] is closed scanned by NTCP")

	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		for port in range(int(how)):
			executor.submit(scan, ip, port + 1)