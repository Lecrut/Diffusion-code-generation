def hex_to_int(hex_str):
    return int(hex_str, 16)

if __name__ == '__main__':
    print(hex_to_int("1a"))
    print(hex_to_int("FF"))
    print(hex_to_int("0"))
    print(hex_to_int("10"))