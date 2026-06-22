def hex_to_decimal(hex_string: str) -> int:
    result = 0
    for char in hex_string:
        value = ord(char)
        if 48 <= value <= 57:
            digit = value - 48
        elif 65 <= value <= 70:
            digit = value - 55
        elif 97 <= value <= 102:
            digit = value - 87
        else:
            raise ValueError(f'Invalid hexadecimal digit: {char}')
        result = result << 4 | digit
    return result
if __name__ == '__main__':
    hex_input = '1A3F'
    decimal_output = hex_to_decimal(hex_input)
    print(decimal_output)