def hex_to_decimal(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    valid_chars = set("0123456789abcdefABCDEF")
    if hex_string.startswith(("0x", "0X")):
        content = hex_string[2:]
        if not content:
            raise ValueError("Hex string cannot contain only prefix")
    else:
        content = hex_string
    for char in content:
        if char not in valid_chars:
            raise ValueError(f"Invalid character '{char}' in hex string")
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ValueError(f"Invalid hex string: {hex_string}")

if __name__ == '__main__':
    test_cases = ["1A", "ff", "0x10", "G1", ""]
    for case in test_cases:
        try:
            result = hex_to_decimal(case)
            print(f"{case} -> {result}")
        except ValueError as e:
            print(f"{case} -> Error: {e}")