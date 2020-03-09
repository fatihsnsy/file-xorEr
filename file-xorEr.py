import sys

if len(sys.argv) != 4:
    print ("Usage %s file key(with hex) outfile"%(sys.argv[0]))
    

xor_file = bytearray(open(sys.argv[1], 'rb').read())           

key = int(sys.argv[2], 16)

size = len(xor_file)
xor_byte_array = bytearray(size)


for i in range(size):
    xor_byte_array[i] = xor_file[i] ^ key

    
open(sys.argv[3], 'wb').write(xor_byte_array)



