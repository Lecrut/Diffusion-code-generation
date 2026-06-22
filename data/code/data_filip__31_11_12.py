def parse_hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        return None
    hex_string = hex_string.strip()
    if not hex_string:
        return None
    if hex_string.startswith(('0x', '0X')):
        hex_part = hex_string[2:]
    else:
        hex_part = hex_string
    if not hex_part:
        return None
    try:
        return int(hex_part, 16)
    except ValueError:
        return None

if __name__ == '__main__':
    print(parse_hex_to_decimal('0xFF'))
    print(parse_hex_to_decimal('0X1A3'))
    print(parse_hex_to_decimal('deadbeef'))
    print(parse_hex_to_decimal('0x0'))
    print(parse_hex_to_decimal('0x'))
    print(parse_hex_to_decimal(''))
    print(parse_hex_to_decimal('not a hex'))
    print(parse_hex_to_decimal('0xGG'))
    print(parse_hex_to_decimal(None))
    print(parse_hex_to_decimal(123))