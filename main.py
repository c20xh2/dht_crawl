import btdht
import binascii
import time


def getinfo(thash):
	test_ip = ''
	i = 0
	while i < 5:
		getpeers = dht.get_peers(binascii.a2b_hex(thash))
		if getpeers:
			if test_ip in getpeers:
				print ("FOUND ME")
		i = i + 1
		time.sleep(30)

dht = btdht.DHT()
dht.start()
i = 0

thash = "8057597c0ea6c4de39cdbc7304c512a3db0695e1"

getinfo(thash)
