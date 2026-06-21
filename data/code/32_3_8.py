BINARY_HEX_MAP = {
    '0': '0', '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6', '7': '7',
    '8': '8', '9': '9', 'a': 'A', 'b': 'B',
    'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    hex_chars = []
    length = len(binary_string)
    padding = (4 - length % 4) % 4
    padded_binary = '0' * padding + binary_string
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i+4]
        hex_chars.append(BINARY_HEX_MAP[chunk])
    return ''.join(hex_chars)

if __name__ == '__main__':
    test_cases = ['1010', '1111', '00010010', '11011111']
    for case in test_cases:
        result = binary_to_hex(case)
        print(f"{case} -> {result}")