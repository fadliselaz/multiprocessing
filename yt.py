import os
import time
import multiprocessing

def sos(x):
	os.system(x)


def op():
	sos("clear")
	sos("/Applications/Epic.app/Contents/MacOS/Epic")
	
def kill():
	time.sleep(20)
	sos("pkill Epic")
	sos("clear")


if __name__ == "__main__":


	# script dibawah akan menjalankan langsung 
	# 2 script diatas secara bersamaan

	p1 = multiprocessing.Process(target=op)
	p2 = multiprocessing.Process(target=kill)


		
	p1.start()
	p2.start()
