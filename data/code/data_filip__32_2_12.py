import binascii

def binary_to_hexadecimal(data: bytes) -> str:
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    return binascii.hexlify(data).decode('ascii')

if __name__ == '__main__':
    sample_binary = b'\x01\x02\x03\x04\x05'
    result = binary_to_hexadecimal(sample_binary)
    print(result)