#!/bin/python3
"""
n = 18721
e = 23
doBreak = False
for p in range(n-1):
	for q in range(n-1):
		if p*q == n:
			i = 1
			value = (p-1)*(q-1)
			while True:
				if i*e % value == 1:
					print("p: {}, q: {}, d: {}".format(p,q,i))
					break
				i += 1

			doBreak = True
			break
	if doBreak:
		break

"""
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(len(abc))
for i in range(0,26):
	print(str(abc[i]) + ": " + str(((i**(25))%18721)))
