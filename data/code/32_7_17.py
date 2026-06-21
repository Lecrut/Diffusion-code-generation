def binary_to_hex(binary_string):
    normalized = binary_string[2:] if binary_string.lower().startswith('0b') else binary_string
    padded = normalized.zfill((len(normalized) + 3) // 4 * 4)
    grouped = [padded[i:i+4] for i in range(0, len(padded), 4)]
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    return ''.join([hex_map[b] for b in grouped])

if __name__ == '__main__':
    print(binary_to_hex('10101010'))
    print(binary_to_hex('11110000'))
    print(binary_to_hex('0b11111111'))