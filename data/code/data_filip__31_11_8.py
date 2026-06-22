def parse_hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        return None
    if len(hex_string) < 3:
        return None
    if hex_string[:2].lower() != "0x":
        return None
    try:
        return int(hex_string, 16)
    except ValueError:
        return None

if __name__ == "__main__":
    test_values = ["0x1A", "0XFF", "0x0", "0xGHI", "123", "", "0x"]
    for val in test_values:
        result = parse_hex_to_decimal(val)
        print(f"Input: '{val}' -> Output: {result}")