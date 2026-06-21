import binascii

def binary_to_hex(data):
    if isinstance(data, str):
        data = bytes(data, 'utf-8')
    if isinstance(data, bytearray):
        data = bytes(data)
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes, bytearray, or string")
    return binascii.hexlify(data).decode('ascii')

if __name__ == '__main__':
    sample_data = b'\x48\x65\x6c\x6c\x6f'
    result = binary_to_hex(sample_data)
    print(result)