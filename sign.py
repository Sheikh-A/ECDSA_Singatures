from fastecdsa.curve import secp256k1
#curve function
from fastecdsa.keys import export_key, gen_keypair
#keys function
from fastecdsa import curve, ecdsa, keys, point
#ecdsa
from hashlib import sha256
#sha256

import random

def sign(m):
	#generate public key
	#Your code here
	private_key, public_key = keys.gen_keypair(secp256k1)

	#generate signature
	#Your code here
	r, s = ecdsa.sign(m, private_key, curve=secp256k1, hashfunc=sha256)

	checkBalance = ecdsa.verify((r,s), m, public_key, curve=secp256k1, hashfunc=sha256)
	print(checkBalance)
	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )
