def hex_to_decimal(hex_string):
    hex_string = hex_string.lstrip('0x').lstrip('0X')
    if not hex_string:
        return 0
    decimal_value = 0
    hex_chars = '0123456789ABCDEF'
    char_to_value = {char: index for index, char in enumerate(hex_chars)}
    hex_string = hex_string.upper()
    for char in hex_string:
        if char not in char_to_value:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        decimal_value = decimal_value * 16 + char_to_value[char]
    return decimal_value

if __name__ == '__main__':
    sample_hex_values = ['1A', 'FF', '0x0', '2F', 'ABCDEF', '0x1a2b3c']
    for hex_val in sample_hex_values:
        result = hex_to_decimal(hex_val)
        print(result)