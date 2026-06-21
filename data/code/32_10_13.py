def binary_to_hex(binary_str):
    value = 0
    for char in binary_str:
        value = (value << 1) | (ord(char) - ord('0'))
    return hex(value)[2:].upper() if value else '0'

if __name__ == '__main__':
    print(binary_to_hex('0000'))
    print(binary_to_hex('10101010'))
    print(binary_to_hex('11110000'))
    print(binary_to_hex('0'))
    print(binary_to_hex('1'))