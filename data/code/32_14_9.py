NIBBLE_MAP = {
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
    if not binary_string:
        return ''
    
    padding_needed = (4 - len(binary_string) % 4) % 4
    if padding_needed:
        binary_string = '0' * padding_needed + binary_string
    
    chunks = (binary_string[i:i+4] for i in range(0, len(binary_string), 4))
    hex_chars = [NIBBLE_MAP.get(chunk, '0') for chunk in chunks]
    
    return ''.join(hex_chars)

if __name__ == '__main__':
    test_input_1 = '10101010'
    test_input_2 = '1111'
    test_input_3 = '00000000'
    test_input_4 = '1'
    
    result_1 = binary_to_hex(test_input_1)
    result_2 = binary_to_hex(test_input_2)
    result_3 = binary_to_hex(test_input_3)
    result_4 = binary_to_hex(test_input_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)