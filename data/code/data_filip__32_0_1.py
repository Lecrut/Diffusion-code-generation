def bin_to_hex(binary_string):
    if not binary_string:
        return '0'
    mapping = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    padding_length = len(binary_string) % 4
    if padding_length > 0:
        binary_string = '0' * (4 - padding_length) + binary_string
    hex_digits = []
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        hex_digits.append(mapping[chunk])
    return ''.join(hex_digits)

if __name__ == '__main__':
    sample_binary_1 = '11010111'
    sample_binary_2 = '10'
    result_1 = bin_to_hex(sample_binary_1)
    result_2 = bin_to_hex(sample_binary_2)
    print(result_1)
    print(result_2)