def binary_to_hex(binary_str):
    hex_digits = '0123456789abcdef'
    padded = binary_str.zfill(len(binary_str) + 3 - (len(binary_str) + 3) % 4)
    groups = [padded[i:i+4] for i in range(0, len(padded), 4)]
    hex_chars = [hex_digits[int(bit, 2)] for bit in groups]
    return '0x' + ''.join(hex_chars).lstrip('0') or '0x0'

if __name__ == '__main__':
    result = binary_to_hex('10101010')
    print(result)