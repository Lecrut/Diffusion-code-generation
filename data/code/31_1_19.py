def hex_to_decimal(hex_string):
    hex_chars = '0123456789abcdef'
    hex_string = hex_string.lower()
    decimal_value = 0
    length = len(hex_string)
    for i, char in enumerate(hex_string):
        if char not in hex_chars:
            raise ValueError("Invalid hexadecimal digit")
        digit_value = hex_chars.index(char)
        position = length - i - 1
        decimal_value += digit_value * (16 ** position)
    return decimal_value

if __name__ == '__main__':
    print(hex_to_decimal('0'))
    print(hex_to_decimal('1A3F'))
    print(hex_to_decimal('ff'))
    print(hex_to_decimal('DEADBEEF'))