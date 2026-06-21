def parse_hex_to_int(hex_string: str) -> int:
    try:
        if not isinstance(hex_string, str):
            raise ValueError("Input must be a string")
        if hex_string.startswith(('0x', '0X')):
            return int(hex_string, 16)
        else:
            raise ValueError("String must be prefixed with '0x' or '0X'")
    except (ValueError, TypeError):
        return 0

if __name__ == '__main__':
    samples = ["0x1A", "0XFF", "0x0", "invalid", "0xG1", "123"]
    for s in samples:
        print(parse_hex_to_int(s))