def parse_hex_to_int(hex_string):
    if not isinstance(hex_string, str):
        return None
    if len(hex_string) < 2:
        return None
    if hex_string[0] == '0' and hex_string[1].lower() == 'x':
        try:
            return int(hex_string, 16)
        except ValueError:
            return None
    return None

if __name__ == '__main__':
    print(parse_hex_to_int('0x1A'))
    print(parse_hex_to_int('0XFF'))
    print(parse_hex_to_int('0x0'))
    print(parse_hex_to_int('0xGHI'))
    print(parse_hex_to_int('123'))
    print(parse_hex_to_int(''))
    print(parse_hex_to_int('0x'))
    print(parse_hex_to_int('0xABCD'))