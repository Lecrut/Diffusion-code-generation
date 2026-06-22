def hex_to_int(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    hex_string = hex_string.strip()
    if hex_string.startswith(("0x", "0X")):
        hex_string = hex_string[2:]
        if not hex_string:
            raise ValueError("Hexadecimal part cannot be empty after '0x' prefix")
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    valid_chars = set("0123456789abcdefABCDEF")
    for char in hex_string:
        if char not in valid_chars:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    return int(hex_string, 16)

if __name__ == '__main__':
    test_cases = [
        "1A",
        "ff",
        "0x10",
        "0XABC",
        "G1",
        "12H",
        "-5",
        ""
    ]
    for case in test_cases:
        try:
            result = hex_to_int(case)
            print(f"{case}: {result}")
        except ValueError as e:
            print(f"{case}: ValueError raised - {e}")