import binascii

def binary_to_hex(binary_string):
    if not binary_string:
        return ""
    if len(binary_string) % 8 != 0:
        padded_length = (len(binary_string) + 7) // 8 * 8
        binary_string = binary_string.zfill(padded_length)
    byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
    return binascii.hexlify(byte_array).decode('ascii').upper()

if __name__ == '__main__':
    sample_binary_1 = "1101101011001110"
    sample_binary_2 = "11111111000000001010101011001100"
    sample_binary_3 = "0"
    result_1 = binary_to_hex(sample_binary_1)
    result_2 = binary_to_hex(sample_binary_2)
    result_3 = binary_to_hex(sample_binary_3)
    print(result_1)
    print(result_2)
    print(result_3)