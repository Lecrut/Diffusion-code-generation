def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        return None
    if hex_string.startswith(('0x', '0X')):
        hex_body = hex_string[2:]
    else:
        hex_body = hex_string
    if not hex_body:
        return None
    try:
        return int(hex_body, 16)
    except ValueError:
        return None

if __name__ == '__main__':
    print(hex_to_decimal('0x1A'))
    print(hex_to_decimal('0XFF'))
    print(hex_to_decimal('0x0'))
    print(hex_to_decimal('0X123ABC'))
    print(hex_to_decimal('0x'))
    print(hex_to_decimal('xyz'))
    print(hex_to_decimal('0xGG'))
    print(hex_to_decimal('1A'))