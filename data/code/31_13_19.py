def hex_to_decimal(hex_string: str) -> int:
    hex_string = hex_string.strip().lower()
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    decimal_value: int = 0
    base: int = 16
    hex_string = hex_string[::-1]
    for index, char in enumerate(hex_string):
        code_point = ord(char)
        digit_value: int = 0
        if 48 <= code_point <= 57:
            digit_value = code_point - 48
        elif 97 <= code_point <= 102:
            digit_value = code_point - 87
        else:
            raise ValueError(f"Invalid character '{char}'")
        decimal_value += digit_value * (base ** index)
    return decimal_value

if __name__ == '__main__':
    input_hex: str = "2A1B"
    output_decimal: int = hex_to_decimal(input_hex)
    print(output_decimal)