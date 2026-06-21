binary_to_hex_lookup = {
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

def binary_to_hex(binary_str):
    if not binary_str:
        return ''
    padded = binary_str.zfill(len(binary_str) + (4 - len(binary_str) % 4) % 4)
    hex_chars = []
    for i in range(0, len(padded), 4):
        nibble = padded[i:i+4]
        hex_chars.append(binary_to_hex_lookup[nibble])
    return ''.join(hex_chars)

if __name__ == '__main__':
    print(binary_to_hex('0'))
    print(binary_to_hex('1'))
    print(binary_to_hex('1010'))
    print(binary_to_hex('11110000'))
    print(binary_to_hex('11011'))