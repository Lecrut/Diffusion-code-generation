def bin_to_hex(binary_string):
    if not binary_string:
        return '0x0'
    while len(binary_string) % 4 != 0:
        binary_string = '0' + binary_string
    nibbles = [binary_string[i:i+4] for i in range(0, len(binary_string), 4)]
    hex_chars = []
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    for nibble in nibbles:
        hex_chars.append(hex_map[nibble])
    return '0x' + ''.join(hex_chars)

if __name__ == '__main__':
    sample_binary = '110101101011'
    result = bin_to_hex(sample_binary)
    print(result)