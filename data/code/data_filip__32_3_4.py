BINARY_TO_HEX = {
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

def binary_to_hex(binary_string):
    if not isinstance(binary_string, str) or not all(c in '01' for c in binary_string):
        raise ValueError("Input must be a binary string")
    if len(binary_string) % 4 != 0:
        binary_string = binary_string.zfill(len(binary_string) + (4 - len(binary_string) % 4))
    result = ''
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        result += BINARY_TO_HEX[chunk]
    return result

if __name__ == '__main__':
    sample_binaries = ['1010', '1111', '110010', '101011011100']
    for b in sample_binaries:
        print(binary_to_hex(b))