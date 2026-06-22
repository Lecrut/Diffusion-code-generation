def hex_to_decimal(hex_string):
    try:
        if not isinstance(hex_string, str):
            return 0
        if len(hex_string) < 3:
            return 0
        prefix = hex_string[:2]
        if prefix not in ('0x', '0X'):
            return 0
        hex_part = hex_string[2:]
        if not hex_part:
            return 0
        valid_chars = set('0123456789abcdefABCDEF')
        if not all(char in valid_chars for char in hex_part):
            return 0
        return int(hex_string, 16)
    except (ValueError, TypeError, OverflowError):
        return 0

if __name__ == '__main__':
    test_cases = [
        '0x1A',
        '0XFF',
        '0x0',
        '0x123ABC',
        '0xZZZ',
        '0x',
        '1A',
        '0x1G',
        '',
        123
    ]
    for case in test_cases:
        print(hex_to_decimal(case))