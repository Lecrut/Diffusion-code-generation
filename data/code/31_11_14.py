def parse_hex_string(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if len(hex_string) < 3:
        raise ValueError("Input string too short to contain a hex prefix")
    if hex_string[:2].lower() != '0x':
        raise ValueError("Input string must start with '0x' or '0X'")
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal string")

if __name__ == '__main__':
    test_values = ["0x1A", "0XFF", "0x0", "0x100"]
    for value in test_values:
        print(parse_hex_string(value))