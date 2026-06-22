def binary_to_hex(binary_string):
    if not binary_string:
        return '0'
    binary_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    length = len(binary_string)
    remainder = length % 4
    if remainder != 0:
        padding = 4 - remainder
        binary_string = '0' * padding + binary_string
    hex_digits = []
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        hex_digits.append(binary_map[chunk])
    result = ''.join(hex_digits)
    while len(result) > 1 and result[0] == '0':
        result = result[1:]
    return '0x' + result

if __name__ == '__main__':
    sample_binaries = ['1010', '11110000', '1', '0000', '110101101']
    for b in sample_binaries:
        print(binary_to_hex(b))