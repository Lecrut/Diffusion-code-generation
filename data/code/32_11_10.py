def convert_binary_to_hex(binary_strings):
    valid_chars = set('01')
    result = []
    for binary_str in binary_strings:
        if not isinstance(binary_str, str):
            raise TypeError(f'Expected string, got {type(binary_str).__name__}')
        if len(binary_str) == 0:
            raise ValueError('Binary string cannot be empty')
        if not valid_chars.issubset(set(binary_str)):
            invalid_chars = set(binary_str) - valid_chars
            raise ValueError(f'Invalid binary characters found: {invalid_chars}')
        decimal_value = int(binary_str, 2)
        hex_value = format(decimal_value, 'X')
        result.append(hex_value)
    return result
if __name__ == '__main__':
    binary_list = ['10101010', '11110000', '1101', '1', '0']
    hex_results = convert_binary_to_hex(binary_list)
    print(hex_results)