def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise TypeError('Input must be a string.')
    hex_string = hex_string.strip()
    negative = False
    if hex_string.startswith('-'):
        negative = True
        hex_string = hex_string[1:]
    if hex_string.lower().startswith('0x'):
        hex_string = hex_string[2:]
    try:
        decimal_value = int(hex_string, 16)
    except ValueError:
        raise ValueError(f'Invalid hexadecimal string: {hex_string}')
    return -decimal_value if negative else decimal_value
if __name__ == '__main__':
    sample_hex_strings = ['1A3F', '0x1A3F', '0X1A3F', '-1A3F', '0', 'FF', 'ff', 'deadBEEF', '  1A3F  ']
    for hex_str in sample_hex_strings:
        try:
            result = hex_to_decimal(hex_str)
            print(f'Hex: {hex_str!r} -> Decimal: {result}')
        except Exception as e:
            print(f'Hex: {hex_str!r} -> Error: {e}')