def hex_to_decimal(hex_string):
    hex_digits = '0123456789ABCDEF'
    decimal_value = 0
    power = 0
    for char in reversed(hex_string.upper()):
        if char not in hex_digits:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        digit_value = hex_digits.index(char)
        decimal_value += digit_value * (16 ** power)
        power += 1
    return decimal_value

if __name__ == '__main__':
    sample_values = ['0', '1A', 'FF', '1F', '10', 'DEADBEEF']
    for sample in sample_values:
        print(hex_to_decimal(sample))