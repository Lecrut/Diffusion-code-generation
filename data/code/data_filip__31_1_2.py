def hex_to_decimal(hex_string):
    hex_string = hex_string.upper()
    if not hex_string:
        return 0
    decimal_value = 0
    length = len(hex_string)
    for i, char in enumerate(hex_string):
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        power = length - 1 - i
        decimal_value += digit * (16 ** power)
    return decimal_value

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)