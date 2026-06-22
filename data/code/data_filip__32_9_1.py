def binary_to_hexadecimal(binary_input: str) -> str:
    if not binary_input:
        return '0'
    if not all((c in '01' for c in binary_input)):
        raise ValueError('Input must contain only binary digits (0 and 1)')
    decimal_value = int(binary_input, 2)
    hex_value = hex(decimal_value)[2:].upper()
    return hex_value
if __name__ == '__main__':
    sample_binary_values = ['1010', '11110000', '0', '1', '1111111111111111', '1010101010101010']
    for binary_val in sample_binary_values:
        result = binary_to_hexadecimal(binary_val)
        print(result)