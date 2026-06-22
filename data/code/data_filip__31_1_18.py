def hex_to_decimal(hex_string):
    hex_digits = '0123456789ABCDEFabcdef'
    if not hex_string:
        return 0
    hex_string = hex_string.upper()
    total = 0
    length = len(hex_string)
    for index, char in enumerate(hex_string):
        if char not in hex_digits:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        digit_value = 0
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit_value = ord(char) - ord('A') + 10
        position_weight = length - index - 1
        total += digit_value * (16 ** position_weight)
    return total

if __name__ == '__main__':
    sample_values = ["1A", "FF", "0", "10", "DEADBEEF"]
    for value in sample_values:
        result = hex_to_decimal(value)
        print(f"Hex: {value}, Decimal: {result}")