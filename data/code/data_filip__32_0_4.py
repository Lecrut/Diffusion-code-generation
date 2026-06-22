def binary_to_hex(binary_string):
    binary_to_hex_map = {
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
    if not binary_string:
        return '0'
    if not all(bit in '01' for bit in binary_string):
        raise ValueError("Input must be a binary string containing only 0 and 1")
    padded_length = ((len(binary_string) + 3) // 4) * 4
    binary_padded = binary_string.zfill(padded_length)
    hex_result = []
    for i in range(0, len(binary_padded), 4):
        nibble = binary_padded[i:i+4]
        hex_result.append(binary_to_hex_map[nibble])
    return ''.join(hex_result)

if __name__ == '__main__':
    print(binary_to_hex('0'))
    print(binary_to_hex('1'))
    print(binary_to_hex('1010'))
    print(binary_to_hex('1111'))
    print(binary_to_hex('11010110'))
    print(binary_to_hex('00000000'))
    print(binary_to_hex('11111111'))
    print(binary_to_hex('101010101010'))