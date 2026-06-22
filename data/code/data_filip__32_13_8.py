def binary_to_hex(binary_string):
    if len(binary_string) % 4 != 0:
        binary_string = binary_string.zfill((len(binary_string) + 3) // 4 * 4)

    hex_map = {
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

    result = ''
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i + 4]
        result += hex_map[chunk]

    return result

if __name__ == '__main__':
    sample_binary = '11010110'
    hex_result = binary_to_hex(sample_binary)
    print(hex_result)

    sample_binary2 = '101011110000'
    hex_result2 = binary_to_hex(sample_binary2)
    print(hex_result2)