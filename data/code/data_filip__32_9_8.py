def binary_to_hex(binary_input: str) -> str:
    if not binary_input:
        return '0'
    decimal_value = int(binary_input, 2)
    hex_value = format(decimal_value, 'X')
    return hex_value
if __name__ == '__main__':
    sample_values = ['1010', '11110000', '11011011', '0', '1', '101010101010']
    for binary_str in sample_values:
        result = binary_to_hex(binary_str)
        print(result)