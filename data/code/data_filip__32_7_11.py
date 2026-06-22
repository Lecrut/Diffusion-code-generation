def binary_to_hex(binary_str):
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    nibbles = [padded[i:i + 4] for i in range(0, len(padded), 4)]
    hex_digits = [hex(int(nibble, 2))[2:].upper() for nibble in nibbles]
    return ''.join(hex_digits)

if __name__ == '__main__':
    samples = ['1010', '11110000', '10000000', '11111111']
    for s in samples:
        print(binary_to_hex(s))