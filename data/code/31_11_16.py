def hex_to_int(hex_str):
    try:
        if not isinstance(hex_str, str):
            return 0
        if len(hex_str) < 3:
            return 0
        if hex_str[:2] != '0x' and hex_str[:2] != '0X':
            return 0
        return int(hex_str, 16)
    except (ValueError, TypeError):
        return 0

if __name__ == '__main__':
    test_values = ['0x1A', '0Xff', '0x0', 'invalid', '0xG1', '123']
    for value in test_values:
        result = hex_to_int(value)
        print(result)