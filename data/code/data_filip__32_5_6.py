import binascii

def binary_to_hex(binary_string):
    byte_length = (len(binary_string) + 7) // 8
    padded_string = binary_string.zfill(byte_length * 8)
    hex_string = binascii.hexlify(bytearray(int(padded_string[i:i+8], 2) for i in range(0, len(padded_string), 8))).decode('ascii')
    return hex_string

if __name__ == '__main__':
    binary_input = "11010110101010101101100110011001"
    result = binary_to_hex(binary_input)
    print(result)