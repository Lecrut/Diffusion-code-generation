def binary_to_hex_list(binary_strings):
    result = []
    for binary_string in binary_strings:
        for char in binary_string:
            if char not in ('0', '1'):
                raise ValueError(f"Invalid binary character '{char}' in '{binary_string}'")
        decimal_value = int(binary_string, 2)
        hex_string = format(decimal_value, 'X')
        result.append(hex_string)
    return result

if __name__ == '__main__':
    sample_binary_strings = [
        '0',
        '1',
        '1010',
        '11110000',
        '11011111'
    ]
    try:
        hex_results = binary_to_hex_list(sample_binary_strings)
        print(hex_results)
    except ValueError as e:
        print(f"Error: {e}")