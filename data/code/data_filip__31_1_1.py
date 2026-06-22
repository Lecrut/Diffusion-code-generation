def hex_to_decimal(hex_str):
    hex_str = hex_str.upper().lstrip('0')
    if not hex_str:
        return 0
    decimal_value = 0
    power = 0
    for char in reversed(hex_str):
        if char.isdigit():
            digit_value = int(char)
        else:
            digit_value = ord(char) - ord('A') + 10
        if not (0 <= digit_value <= 15):
            raise ValueError(f"Invalid hexadecimal character: {char}")
        decimal_value += digit_value * (16 ** power)
        power += 1
    return decimal_value

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)