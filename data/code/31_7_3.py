from functools import reduce

def hex_to_decimal(hex_str):
    return reduce(lambda acc, char: acc * 16 + int(char, 16), hex_str, 0)

if __name__ == '__main__':
    print(hex_to_decimal("1A3"))
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("0"))
    print(hex_to_decimal("DEADBEEF"))