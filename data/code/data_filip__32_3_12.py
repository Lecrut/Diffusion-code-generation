def binary_to_hex(binary_string):
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
        '1111': 'F'
    }
    if not binary_string:
        return '0'
    padded_binary = binary_string.zfill((len(binary_string) + 3) // 4 * 4)
    hex_digits = []
    for i in range(0, len(padded_binary), 4):
        nibble = padded_binary[i:i+4]
        hex_digits.append(lookup[nibble])
    return ''.join(hex_digits)

if __name__ == '__main__':
    sample_binary_1 = '1010'
    sample_binary_2 = '11110000'
    sample_binary_3 = '1010101010'
    print(binary_to_hex(sample_binary_1))
    print(binary_to_hex(sample_binary_2))
    print(binary_to_hex(sample_binary_3))