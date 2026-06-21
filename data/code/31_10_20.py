def hex_to_decimal(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise TypeError('Input must be a string')
    hex_string = hex_string.strip()
    if not hex_string:
        raise ValueError('Input string is empty')
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    if not hex_string:
        raise ValueError('Invalid hexadecimal string')
    for char in hex_string:
        if char.lower() not in '0123456789abcdef':
            raise ValueError(f'Invalid hexadecimal digit: {char}')
    decimal_value = 0
    hex_digits = '0123456789abcdef'
    for char in hex_string.lower():
        decimal_value = decimal_value * 16
        index = hex_digits.index(char)
        decimal_value += index
    return decimal_value
if __name__ == '__main__':
    sample_values = ['1A', 'FF', '0x2F', '0X10', 'deadbeef', '0', 'A', '123456789ABCDEF']
    for hex_str in sample_values:
        decimal_result = hex_to_decimal(hex_str)
        print(f"hex_to_decimal('{hex_str}') = {decimal_result}")