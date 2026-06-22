def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        return 0
    if len(hex_string) < 2:
        return 0
    if hex_string[:2].lower() != '0x':
        return 0
    try:
        return int(hex_string, 16)
    except ValueError:
        return 0

if __name__ == '__main__':
    print(hex_to_decimal("0x1A"))
    print(hex_to_decimal("0XFF"))
    print(hex_to_decimal("0xGHI"))
    print(hex_to_decimal("123"))
    print(hex_to_decimal(""))
    print(hex_to_decimal(None))