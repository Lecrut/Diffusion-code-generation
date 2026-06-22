def binary_to_hex(binary_string: str) -> str:
    binary_string = binary_string.lstrip('0')
    if not binary_string:
        return '0'
    decimal_value = int(binary_string, 2)
    hex_string = format(decimal_value, 'X')
    return hex_string

if __name__ == '__main__':
    sample_1 = '1010'
    sample_2 = '00001111'
    sample_3 = '0'
    sample_4 = '1101011010110101'
    
    result_1 = binary_to_hex(sample_1)
    result_2 = binary_to_hex(sample_2)
    result_3 = binary_to_hex(sample_3)
    result_4 = binary_to_hex(sample_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)