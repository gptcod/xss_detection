# -*- encoding: UTF-8 -*-


import binascii

serial = b"5B134977135E7D13"
name = ""

key = [0x10, 0x20, 0x30]

for i, c in enumerate(binascii.unhexlify(serial)):
    name += chr(c ^ key[i % len(key)])

print(name)
