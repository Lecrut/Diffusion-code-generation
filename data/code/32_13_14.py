def binary_to_hex(binary_string):
    if not binary_string:
        return ''
    padded_binary = binary_string.zfill((len(binary_string) + 3) // 4 * 4)
    hex_digits = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i + 4]
        value = int(chunk, 2)
        hex_digits.append(format(value, 'x'))
    return ''.join(hex_digits)
if __name__ == '__main__':
    sample_binaries = ['10101011', '1111000011110000', '111', '0', '1', '1111111111111111', '1000000000000001']
    for binary_str in sample_binaries:
        result = binary_to_hex(binary_str)
        print(f'Binary: {binary_str} -> Hex: {result}')