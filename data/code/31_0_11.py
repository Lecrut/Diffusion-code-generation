def hex_to_decimal(hex_str):
    return int(hex_str, 16)

if __name__ == '__main__':
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("1A3"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("10"))
    print(hex_to_decimal("BEEF"))