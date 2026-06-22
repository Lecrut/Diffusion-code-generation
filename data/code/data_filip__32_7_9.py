def binary_to_hex(binary_str):
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    nibbles = [padded[i:i + 4] for i in range(0, len(padded), 4)]
    hex_chars = [format(int(nib, 2), 'x') for nib in nibbles]
    return ''.join(hex_chars)

if __name__ == '__main__':
    sample_values = ['1010', '11110000', '101010101010', '1', '1111']
    results = [binary_to_hex(val) for val in sample_values]
    for binary_val, hex_val in zip(sample_values, results):
        print(f"{binary_val} -> {hex_val}")