def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    if hex_string.startswith('-'):
        negative = True
        hex_string = hex_string[1:]
    else:
        negative = False
    decimal_value = 0
    for char in hex_string:
        decimal_value *= 16
        if '0' <= char <= '9':
            decimal_value += ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            decimal_value += ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            decimal_value += ord(char) - ord('A') + 10
        else:
            raise ValueError("Invalid hexadecimal digit")
    if negative:
        decimal_value = -decimal_value
    return decimal_value

if __name__ == '__main__':
    print(hex_to_decimal('1a'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0x0'))
    print(hex_to_decimal('-1a'))
    print(hex_to_decimal('DEADBEEF'))