def binary_to_hex(binary_str):
    if not binary_str:
        return '0'
    if not all(c in '01' for c in binary_str):
        raise ValueError("Input must be a binary string containing only '0' and '1'")
    num = int(binary_str, 2)
    hex_str = hex(num)[2:].upper()
    return hex_str

if __name__ == '__main__':
    print(binary_to_hex('0'))
    print(binary_to_hex('1'))
    print(binary_to_hex('1010'))
    print(binary_to_hex('1111'))
    print(binary_to_hex('00001010'))
    print(binary_to_hex('11010110'))
    print(binary_to_hex(''))