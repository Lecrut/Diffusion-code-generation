def hex_to_decimal(hex_string):
    if not hex_string:
        return 0
    hex_string = hex_string.strip().lower()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    valid_chars = '0123456789abcdef'
    for char in hex_string:
        if char not in valid_chars:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    decimal_value = 0
    length = len(hex_string)
    for i in range(length):
        char = hex_string[i]
        if char in '0123456789':
            digit_value = ord(char) - ord('0')
        else:
            digit_value = ord(char) - ord('a') + 10
        exponent = length - 1 - i
        decimal_value += digit_value * (16 ** exponent)
    return decimal_value

if __name__ == '__main__':
    sample_hex_values = ["1A3F", "0", "FF", "10", "ABCDEF"]
    for hex_val in sample_hex_values:
        result = hex_to_decimal(hex_val)
        print(f"{hex_val}: {result}")