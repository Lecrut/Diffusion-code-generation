def parse_hex_to_int(hex_string):
    if not isinstance(hex_string, str):
        return 0
    stripped = hex_string.strip()
    if stripped.startswith(('0x', '0X')):
        part = stripped[2:]
    else:
        part = stripped
    if not part:
        return 0
    try:
        return int(part, 16)
    except ValueError:
        return 0

if __name__ == '__main__':
    print(parse_hex_to_int("0x1A"))
    print(parse_hex_to_int("0XFF"))
    print(parse_hex_to_int("abc"))
    print(parse_hex_to_int("0x"))
    print(parse_hex_to_int(""))
    print(parse_hex_to_int("0xGHI"))
    print(parse_hex_to_int("10"))