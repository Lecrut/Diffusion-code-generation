def binary_to_hex(binary_str: str) -> str:
    num = int(binary_str, 2)
    if num == 0:
        return '0'
    hex_digits = '0123456789ABCDEF'
    result = []
    while num > 0:
        result.append(hex_digits[num & 0xF])
        num >>= 4
    return ''.join(reversed(result))

if __name__ == '__main__':
    print(binary_to_hex("11010110101"))
    print(binary_to_hex("0000"))
    print(binary_to_hex("1111"))