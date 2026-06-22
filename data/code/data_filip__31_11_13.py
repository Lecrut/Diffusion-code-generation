def parse_hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        return None
    if not hex_string:
        return None
    if hex_string.startswith(('0x', '0X')):
        hex_content = hex_string[2:]
    else:
        return None
    if not hex_content:
        return None
    try:
        return int(hex_content, 16)
    except ValueError:
        return None

if __name__ == '__main__':
    print(parse_hex_to_decimal('0x1A'))
    print(parse_hex_to_decimal('0XFF'))
    print(parse_hex_to_decimal('0x0'))
    print(parse_hex_to_decimal('0xGHI'))
    print(parse_hex_to_decimal(''))
    print(parse_hex_to_decimal('1A'))
    print(parse_hex_to_decimal(None))
    print(parse_hex_to_decimal(123))