def binary_to_hex(binary_str):
    hex_chars = '0123456789abcdef'
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    groups = [padded[i:i+4] for i in range(0, len(padded), 4)]
    hex_digits = [hex_chars[int(group, 2)] for group in groups]
    hex_str = ''.join(hex_digits)
    hex_str = hex_str.lstrip('0')
    return hex_str if hex_str else '0'

if __name__ == '__main__':
    result = binary_to_hex('1101011010')
    print(result)