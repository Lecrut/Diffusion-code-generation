def parse_hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        return None
    if len(hex_string) < 2:
        return None
    if not (hex_string.startswith('0x') or hex_string.startswith('0X')):
        return None
    hex_digits = hex_string[2:]
    if not hex_digits:
        return None
    try:
        return int(hex_digits, 16)
    except ValueError:
        return None

if __name__ == '__main__':
    sample_values = [
        '0x1A',
        '0XFF',
        '0x0',
        '0xGHI',
        '0x',
        'xyz',
        '123',
        '0x10',
        '0XdeadBEEF'
    ]
    for value in sample_values:
        print(parse_hex_to_decimal(value))