BINARY_TO_HEX = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

def binary_to_hex(binary_string):
    binary_string = binary_string.replace(' ', '')
    length = len(binary_string)
    remainder = length % 4
    if remainder != 0:
        binary_string = '0' * (4 - remainder) + binary_string
    hex_result = []
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        hex_result.append(BINARY_TO_HEX[chunk])
    return ''.join(hex_result)

if __name__ == '__main__':
    sample_binary = "110101101111"
    result = binary_to_hex(sample_binary)
    print(result)
    sample_binary_2 = "00001111"
    result_2 = binary_to_hex(sample_binary_2)
    print(result_2)