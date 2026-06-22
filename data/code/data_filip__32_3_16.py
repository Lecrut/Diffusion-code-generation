def binary_to_hex_map():
    bin_to_hex = {
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
    return bin_to_hex

def binary_to_hex(binary_str):
    lookup = binary_to_hex_map()
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    hex_digits = []
    for i in range(0, len(padded), 4):
        chunk = padded[i:i+4]
        hex_digits.append(lookup[chunk])
    return ''.join(hex_digits)

if __name__ == '__main__':
    sample_binaries = ['10101010', '1111', '100000000000', '1101']
    for bin_val in sample_binaries:
        result = binary_to_hex(bin_val)
        print(result)