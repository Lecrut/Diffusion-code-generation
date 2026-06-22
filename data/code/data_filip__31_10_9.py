def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise TypeError('Input must be a string.')
    cleaned_hex = hex_string.strip()
    if not cleaned_hex:
        raise ValueError('Input string is empty.')
    try:
        return int(cleaned_hex, 16)
    except ValueError as e:
        raise ValueError(f'Invalid hexadecimal string: {hex_string}') from e
if __name__ == '__main__':
    sample_values = ['0x1A', 'FF', 'deadBEEF', '0', '123456789ABCDEF', '0x0', '10']
    for hex_str in sample_values:
        decimal_value = hex_to_decimal(hex_str)
        print(f'{hex_str}: {decimal_value}')