def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    
    binary_string = binary_string.lstrip('0')
    if not binary_string:
        return "0"
    
    pad_length = len(binary_string) % 4
    if pad_length:
        binary_string = '0' * (4 - pad_length) + binary_string
    
    hex_digits = {
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
        '1010': 'a',
        '1011': 'b',
        '1100': 'c',
        '1101': 'd',
        '1110': 'e',
        '1111': 'f'
    }
    
    hex_result = []
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        hex_result.append(hex_digits[chunk])
    
    return ''.join(hex_result)

if __name__ == '__main__':
    sample_binary = "11010110"
    result = binary_to_hex(sample_binary)
    print(result)
    sample_binary_2 = "1010"
    result_2 = binary_to_hex(sample_binary_2)
    print(result_2)
    sample_binary_3 = "0000"
    result_3 = binary_to_hex(sample_binary_3)
    print(result_3)
    sample_binary_4 = "11111111"
    result_4 = binary_to_hex(sample_binary_4)
    print(result_4)