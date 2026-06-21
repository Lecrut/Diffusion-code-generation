def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    hex_chars = '0123456789ABCDEFabcdef'
    for char in hex_string:
        if char not in hex_chars:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    decimal_value = 0
    power = len(hex_string) - 1
    for char in hex_string:
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit_value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit_value = ord(char) - ord('A') + 10
        decimal_value += digit_value * (16 ** power)
        power -= 1
    return decimal_value

if __name__ == '__main__':
    sample_value = "1A3F"
    result = hex_to_decimal(sample_value)
    print(result)
    sample_value_2 = "FF"
    result_2 = hex_to_decimal(sample_value_2)
    print(result_2)
    sample_value_3 = "0"
    result_3 = hex_to_decimal(sample_value_3)
    print(result_3)