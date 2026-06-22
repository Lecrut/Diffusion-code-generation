import binascii

def binary_to_hex(binary_input):
    if isinstance(binary_input, str):
        if binary_input.startswith('0b') or binary_input.startswith('0B'):
            bytes_val = int(binary_input, 2).to_bytes((len(binary_input) - 2 + 7) // 8, byteorder='big')
        else:
            padded = binary_input.zfill((len(binary_input) + 7) // 8 * 8)
            bytes_val = int(padded, 2).to_bytes(len(padded) // 8, byteorder='big')
    elif isinstance(binary_input, bytes):
        bytes_val = binary_input
    elif isinstance(binary_input, bytearray):
        bytes_val = bytes(binary_input)
    elif isinstance(binary_input, int):
        if binary_input < 0:
            bit_length = binary_input.bit_length() + 1
            bytes_val = binary_input.to_bytes((bit_length + 7) // 8, byteorder='big', signed=True)
        else:
            if binary_input == 0:
                return "0"
            bytes_val = binary_input.to_bytes((binary_input.bit_length() + 7) // 8, byteorder='big')
    else:
        raise TypeError("Unsupported type for binary input")

    return binascii.hexlify(bytes_val).decode('ascii')

if __name__ == '__main__':
    print(binary_to_hex("1111"))
    print(binary_to_hex(b'\xff\xfe'))
    print(binary_to_hex(10))