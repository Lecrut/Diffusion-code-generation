def hex_to_decimal(hex_str):
    hex_str = hex_str.strip()
    is_negative = False
    if hex_str.startswith('-'):
        is_negative = True
        hex_str = hex_str[1:]
    
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    
    if not hex_str:
        return 0
    
    decimal_value = 0
    hex_chars = "0123456789ABCDEF"
    
    for char in hex_str:
        upper_char = char.upper()
        if upper_char in hex_chars:
            digit = hex_chars.index(upper_char)
            decimal_value = decimal_value * 16 + digit
        else:
            raise ValueError(f"Invalid hexadecimal digit: {char}")
    
    if is_negative:
        decimal_value = -decimal_value
    
    return decimal_value

def decimal_to_hex(decimal_value):
    if decimal_value == 0:
        return "0"
    
    is_negative = decimal_value < 0
    decimal_value = abs(decimal_value)
    
    hex_chars = "0123456789ABCDEF"
    result = []
    
    while decimal_value > 0:
        remainder = decimal_value % 16
        result.append(hex_chars[remainder])
        decimal_value //= 16
    
    if is_negative:
        result.append('-')
    
    return ''.join(reversed(result))

if __name__ == '__main__':
    test_hex_values = ["FF", "ff", "1A2B", "0x1F", "0X1f", "0", "-10", "-FF"]
    test_decimal_values = [255, 255, 6699, 31, 31, 0, -16, -255]
    
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("ff"))
    print(hex_to_decimal("1A2B"))
    print(hex_to_decimal("0x1F"))
    print(hex_to_decimal("0X1f"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("-10"))
    print(hex_to_decimal("-FF"))
    print(decimal_to_hex(255))
    print(decimal_to_hex(-255))
    print(decimal_to_hex(0))
    print(decimal_to_hex(6699))