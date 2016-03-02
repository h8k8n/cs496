import zlib
import hashlib

print(type(zlib.crc32(bytes(1))&65535))
#print(binascii.crc32(b"1")&65535)

#print(hash('1'))

for i in range(65535):
    for j in range(65535):
        if((i!=0) and (i != j) and (zlib.crc32(bytes(i))&65535) == (zlib.crc32(bytes(j))&65535)):
            print(zlib.crc32(bytes(i)), zlib.crc32(bytes(j)), i, j)
            print('hello')

