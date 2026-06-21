def validate_and_convert_to_hex(binary_string):
    if not isinstance(binary_string, str):
        raise TypeError("Input must be a string")
    valid_chars = set('01')
    for char in binary_string:
        if char not in valid_chars:
            raise ValueError(f"Invalid binary character: {char}")
    decimal_value = int(binary_string, 2)
    hex_value = hex(decimal_value)[2:].upper()
    return hex_value

if __name__ == '__main__':
    sample_values = ['1010', '11110000', '0', '1', '101010']
    for val in sample_values:
        print(validate_and_convert_to_hex(val))
    try:
        validate_and_convert_to_hex('1020')
    except ValueError as e:
        print(e)
    try:
        validate_and_convert_to_hex('')
    except ValueError as e:
        print(e)