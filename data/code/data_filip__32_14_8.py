import sys

def binary_string_to_hex(binary_string):
    if not binary_string:
        return "0"
    
    length = len(binary_string)
    if length % 4 != 0:
        padding_length = 4 - (length % 4)
        binary_string = '0' * padding_length + binary_string
    
    hex_chars = []
    for i in range(0, length, 4):
        nibble = binary_string[i:i+4]
        decimal_value = int(nibble, 2)
        hex_chars.append(format(decimal_value, 'x'))
    
    return ''.join(hex_chars)

if __name__ == '__main__':
    sample_input_1 = "1101011100111000"
    sample_input_2 = "1"
    sample_input_3 = "11111111"
    sample_input_4 = "000000000000"
    
    result_1 = binary_string_to_hex(sample_input_1)
    print(result_1)
    
    result_2 = binary_string_to_hex(sample_input_2)
    print(result_2)
    
    result_3 = binary_string_to_hex(sample_input_3)
    print(result_3)
    
    result_4 = binary_string_to_hex(sample_input_4)
    print(result_4)