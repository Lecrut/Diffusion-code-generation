def hex_to_decimal(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise TypeError("Input must be a string")
    hex_string = hex_string.strip()
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    is_negative = False
    if hex_string.startswith('-'):
        is_negative = True
        hex_string = hex_string[1:]
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    if not hex_string:
        raise ValueError("No hexadecimal digits found")
    valid_chars = set("0123456789abcdefABCDEF")
    for char in hex_string:
        if char not in valid_chars:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    result = int(hex_string, 16)
    if is_negative:
        result = -result
    return result

if __name__ == '__main__':
    test_cases = ["0x1A", "1A", "0xFF", "ff", "-0x10", "0XdeadBEEF"]
    for case in test_cases:
        print(hex_to_decimal(case))