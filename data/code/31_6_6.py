def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
        if not hex_string:
            raise ValueError("Input string cannot be empty after stripping prefix")
    for char in hex_string:
        if char not in '0123456789abcdefABCDEF':
            raise ValueError(f"Invalid character '{char}' in hex string")
    return int(hex_string, 16)

if __name__ == '__main__':
    test_cases = ["1A", "0xFF", "g1", ""]
    for case in test_cases:
        try:
            result = hex_to_decimal(case)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")