def parse_hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        return 0
    if len(hex_string) < 2:
        return 0
    prefix = hex_string[:2].lower()
    if prefix != '0x':
        return 0
    hex_digits = hex_string[2:]
    if not hex_digits:
        return 0
    try:
        return int(hex_digits, 16)
    except ValueError:
        return 0

if __name__ == '__main__':
    print(parse_hex_to_decimal('0x1A'))
    print(parse_hex_to_decimal('0XFF'))
    print(parse_hex_to_decimal('0x0'))
    print(parse_hex_to_decimal('0xGHI'))
    print(parse_hex_to_decimal('abc'))
    print(parse_hex_to_decimal('0x'))
    print(parse_hex_to_decimal(''))
    print(parse_hex_to_decimal(None))