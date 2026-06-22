def hex_string_to_int(hex_str):
    valid_hex_chars = set('0123456789abcdefABCDEF')
    if not isinstance(hex_str, str):
        raise ValueError("Input must be a string")
    if len(hex_str) == 0:
        raise ValueError("Input string cannot be empty")
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
        if len(hex_str) == 0:
            raise ValueError("Hex string is empty after removing '0x' prefix")
    if any(char not in valid_hex_chars for char in hex_str):
        raise ValueError("Invalid hexadecimal string")
    return int(hex_str, 16)

if __name__ == '__main__':
    test_cases = ["FF", "1A3F", "0xFF", "deadBEEF", "0x10", "ZZ", ""]
    for case in test_cases:
        try:
            result = hex_string_to_int(case)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")