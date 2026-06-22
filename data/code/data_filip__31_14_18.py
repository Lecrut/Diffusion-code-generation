def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    elif hex_string.startswith('-'):
        sign = -1
        hex_string = hex_string[1:]
        if hex_string.startswith('0x') or hex_string.startswith('0X'):
            hex_string = hex_string[2:]
    else:
        sign = 1

    if not hex_string:
        return 0

    decimal_value = 0
    hex_digits = '0123456789abcdef'
    hex_upper = '0123456789ABCDEF'

    for char in hex_string:
        lower_char = char.lower()
        if lower_char in hex_digits:
            digit_value = hex_digits.index(lower_char)
        elif char in hex_upper:
            digit_value = hex_upper.index(char)
        else:
            raise ValueError("Invalid hexadecimal digit: {}".format(char))
        decimal_value = decimal_value * 16 + digit_value

    return sign * decimal_value

if __name__ == '__main__':
    print(hex_to_decimal('1A3'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0x2F'))
    print(hex_to_decimal('-1A3'))
    print(hex_to_decimal('0'))
    print(hex_to_decimal('DEADBEEF'))