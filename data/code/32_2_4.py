import binascii

def binary_to_hex(binary_input):
    binary_str = ''.join(str(int(b)) for b in binary_input)
    if not binary_str:
        return ""
    while len(binary_str) % 4 != 0:
        binary_str = '0' + binary_str
    return binascii.hexlify(int(binary_str, 2).to_bytes((len(binary_str) + 7) // 8, 'big')).decode('ascii')

if __name__ == '__main__':
    sample_binary = [1, 0, 1, 0, 1, 1, 0, 1]
    result = binary_to_hex(sample_binary)
    print(result)