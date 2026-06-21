def hex_to_decimal(hex_string):
    hex_string = hex_string.upper()
    hex_chars = "0123456789ABCDEF"
    total = 0
    for i, char in enumerate(reversed(hex_string)):
        if char not in hex_chars:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        digit_value = hex_chars.index(char)
        positional_weight = 16 ** i
        total += digit_value * positional_weight
    return total

if __name__ == '__main__':
    sample_values = ["1A3F", "FF", "0", "10", "DEADBEEF"]
    for sample in sample_values:
        result = hex_to_decimal(sample)
        print(result)