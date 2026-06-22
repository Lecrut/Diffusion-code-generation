import binascii

def binary_to_hex(binary_str: str) -> str:
    if not binary_str:
        return ""
    if len(binary_str) % 4 != 0:
        padding_length = 4 - (len(binary_str) % 4)
        binary_str = "0" * padding_length + binary_str
    hex_bytes = int(binary_str, 2).to_bytes((len(binary_str) + 7) // 8, byteorder='big')
    return binascii.hexlify(hex_bytes).decode('ascii')

if __name__ == '__main__':
    sample_binary = "110101101011"
    result = binary_to_hex(sample_binary)
    print(result)
    sample_binary_large = "1" * 10000
    result_large = binary_to_hex(sample_binary_large)
    print(result_large[:32])
    print(result_large[-32:])