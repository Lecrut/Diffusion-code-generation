def parse_hex_string(hex_str):
    try:
        if not isinstance(hex_str, str):
            return 0
        if len(hex_str) < 2:
            return 0
        if hex_str.startswith('0x') or hex_str.startswith('0X'):
            return int(hex_str, 16)
        return 0
    except (ValueError, TypeError):
        return 0

if __name__ == '__main__':
    test_values = ['0x1A', '0XFF', '0x0', 'invalid', '', '0xG1']
    for val in test_values:
        result = parse_hex_string(val)
        print(f"Input: {val}, Output: {result}")