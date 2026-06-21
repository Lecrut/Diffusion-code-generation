def hex_to_decimal(hex_string):
    return int(hex_string, 16)

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("100"))