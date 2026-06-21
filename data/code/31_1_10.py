def hex_to_decimal(hex_string):
    hex_string = hex_string.upper()
    hex_chars = "0123456789ABCDEF"
    result = 0
    for i, char in enumerate(hex_string):
        if char not in hex_chars:
            raise ValueError("Invalid hexadecimal character")
        digit_value = hex_chars.index(char)
        position = len(hex_string) - 1 - i
        result += digit_value * (16 ** position)
    return result

if __name__ == '__main__':
    sample_values = ["1A", "FF", "10", "0", "ABCDEF", "1234567890ABCDEF"]
    for sample in sample_values:
        print(hex_to_decimal(sample))