def binary_to_hex(binary_digits):
    lookup = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F',
    }
    padded = binary_digits.zfill((len(binary_digits) + 3) // 4 * 4)
    hex_chars = []
    for i in range(0, len(padded), 4):
        nibble = padded[i:i + 4]
        hex_chars.append(lookup[nibble])
    return ''.join(hex_chars)

if __name__ == '__main__':
    print(binary_to_hex('11110101'))
    print(binary_to_hex('1010'))
    print(binary_to_hex('0'))