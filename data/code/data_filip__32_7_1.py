def binary_to_hex(binary_string):
    padded = binary_string.zfill((len(binary_string) + 3) // 4 * 4)
    grouped = [padded[i:i+4] for i in range(0, len(padded), 4)]
    hex_map = {f'{i:04b}': hex(i)[2:] for i in range(16)}
    return ''.join(hex_map[group] for group in grouped)

if __name__ == '__main__':
    samples = ['1010', '11110000', '101010101010']
    for s in samples:
        print(binary_to_hex(s))