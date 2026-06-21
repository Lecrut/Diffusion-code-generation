def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    is_negative = False
    if hex_string[0] == '-':
        is_negative = True
        hex_string = hex_string[1:]
    hex_chars = '0123456789abcdef'
    value = 0
    for char in hex_string.lower():
        if char not in hex_chars:
            raise ValueError("Invalid hexadecimal string")
        digit_value = hex_chars.index(char)
        value = value * 16 + digit_value
    if is_negative:
        value = -value
    return value

if __name__ == '__main__':
    print(hex_to_decimal('0xFF'))
    print(hex_to_decimal('1A3'))
    print(hex_to_decimal('0x0'))
    print(hex_to_decimal('deadBEEF'))
    print(hex_to_decimal('-0x10'))
    print(hex_to_decimal('7F'))