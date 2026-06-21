def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    hex_string = hex_string.lower()
    decimal_value = 0
    for char in hex_string:
        decimal_value *= 16
        if '0' <= char <= '9':
            decimal_value += ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            decimal_value += ord(char) - ord('a') + 10
        else:
            raise ValueError("Invalid hexadecimal digit")
    return decimal_value

if __name__ == '__main__':
    print(hex_to_decimal('1A3'))
    print(hex_to_decimal('0xFF'))
    print(hex_to_decimal('0'))
    print(hex_to_decimal('deadBEEF'))