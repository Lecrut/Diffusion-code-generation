def hex_to_int(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    if hex_string.startswith("0x") or hex_string.startswith("0X"):
        hex_string = hex_string[2:]
    if not hex_string:
        raise ValueError("Hex string cannot be empty after stripping prefix")
    valid_chars = set("0123456789abcdefABCDEF")
    for char in hex_string:
        if char not in valid_chars:
            raise ValueError(f"Invalid character '{char}' in hex string")
    return int(hex_string, 16)

if __name__ == '__main__':
    test_values = ["1A", "0xFF", "7b", "G1", ""]
    for val in test_values:
        try:
            result = hex_to_int(val)
            print(f"Hex '{val}' -> Decimal {result}")
        except ValueError as e:
            print(f"Hex '{val}' raised ValueError: {e}")