def hex_string_to_int(hex_str: str) -> int:
    return int(hex_str, 16)

if __name__ == '__main__':
    print(hex_string_to_int('1a2b'))
    print(hex_string_to_int('0xff'))
    print(hex_string_to_int('0'))
    print(hex_string_to_int('10'))