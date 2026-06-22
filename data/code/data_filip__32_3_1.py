BINARY_TO_HEX_MAP = {
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

def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return '0'
    padding_length = (4 - len(binary_string) % 4) % 4
    padded_binary = '0' * padding_length + binary_string
    hex_digits = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i + 4]
        hex_digits.append(BINARY_TO_HEX_MAP[chunk])
    return ''.join(hex_digits)

if __name__ == '__main__':
    sample_binary = '110101101001'
    result = binary_to_hex(sample_binary)
    print(result)