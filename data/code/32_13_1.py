def bin_to_hex(binary_string):
    binary_string = binary_string.lstrip('0b')
    padding = (4 - len(binary_string) % 4) % 4
    binary_string = '0' * padding + binary_string
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    hex_result = ''
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        hex_result += hex_map[chunk]
    return hex_result

if __name__ == '__main__':
    sample_binary = '11010111100101'
    print(bin_to_hex(sample_binary))