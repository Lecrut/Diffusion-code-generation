def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    is_negative = False
    if hex_string.startswith('-'):
        is_negative = True
        hex_string = hex_string[1:]
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    
    decimal_value = 0
    hex_digits = "0123456789abcdef"
    hex_string = hex_string.lower()
    
    length = len(hex_string)
    for char in hex_string:
        if char not in hex_digits:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        decimal_value = decimal_value * 16 + hex_digits.index(char)
    
    if is_negative:
        return -decimal_value
    return decimal_value

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("0xFF"))
    print(hex_to_decimal("-10"))
    print(hex_to_decimal("10"))