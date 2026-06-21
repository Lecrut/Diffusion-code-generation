def hex_to_decimal(hex_string):
    hex_string = hex_string.upper().strip()
    if hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    result = 0
    length = len(hex_string)
    for i, char in enumerate(hex_string):
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            return None
        weight = 16 ** (length - 1 - i)
        result += digit * weight
    return result

if __name__ == '__main__':
    sample_hex = "1A3F"
    decimal_value = hex_to_decimal(sample_hex)
    print(decimal_value)