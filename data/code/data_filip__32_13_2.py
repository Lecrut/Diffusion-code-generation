def binary_to_hex(binary_string):
    padded_binary = binary_string.zfill((len(binary_string) + 3) // 4 * 4)
    hex_digits = '0123456789ABCDEF'
    hex_result = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i + 4]
        decimal_value = int(chunk, 2)
        hex_result.append(hex_digits[decimal_value])
    return ''.join(hex_result)
if __name__ == '__main__':
    sample_binaries = ['11110000', '10101010', '11011100', '00001111', '11111111', '10000000', '00000001', '1111000011110000', '1', '1010', '1111111111111111']
    for binary_val in sample_binaries:
        hex_val = binary_to_hex(binary_val)
        print(f'Binary: {binary_val} -> Hex: {hex_val}')