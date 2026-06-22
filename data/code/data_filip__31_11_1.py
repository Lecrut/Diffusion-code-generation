def parse_hex_to_int(hex_str):
    if isinstance(hex_str, str) and len(hex_str) > 1 and hex_str[:2] in ('0x', '0X'):
        digits = hex_str[2:]
        if not digits:
            return 0
        try:
            return int(digits, 16)
        except ValueError:
            return 0
    if isinstance(hex_str, str):
        try:
            return int(hex_str, 16)
        except ValueError:
            return 0
    if isinstance(hex_str, (int, float)):
        return int(hex_str)
    return 0

if __name__ == '__main__':
    print(parse_hex_to_int('0x1A'))
    print(parse_hex_to_int('0xFF'))
    print(parse_hex_to_int('0x0'))
    print(parse_hex_to_int('0x00'))
    print(parse_hex_to_int('0x'))
    print(parse_hex_to_int('0xG1'))
    print(parse_hex_to_int(255))
    print(parse_hex_to_int('1F'))