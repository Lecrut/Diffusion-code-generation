def binary_to_hex(binary_str: str) -> str:
    if not binary_str:
        return ""
    padded_len = len(binary_str) + (4 - len(binary_str) % 4) % 4
    binary_str = binary_str.zfill(padded_len)
    hex_digits = '0123456789abcdef'
    result = []
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i+4]
        decimal_val = int(nibble, 2)
        result.append(hex_digits[decimal_val])
    return ''.join(result)

if __name__ == '__main__':
    print(binary_to_hex('11110101101010111010'))