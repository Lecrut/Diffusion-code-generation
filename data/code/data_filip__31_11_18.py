def parse_hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        return None
    if len(hex_string) < 2:
        return None
    prefix = hex_string[:2].lower()
    if prefix != '0x':
        return None
    hex_body = hex_string[2:]
    if not hex_body:
        return None
    try:
        return int(hex_body, 16)
    except ValueError:
        return None

if __name__ == '__main__':
    print(parse_hex_to_decimal('0x1A'))
    print(parse_hex_to_decimal('0XFF'))
    print(parse_hex_to_decimal('0x0'))
    print(parse_hex_to_decimal('0xGHI'))
    print(parse_hex_to_decimal('0x'))
    print(parse_hex_to_decimal('FF'))
    print(parse_hex_to_decimal(None))
    print(parse_hex_to_decimal(123))