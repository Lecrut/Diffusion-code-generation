from functools import reduce

def hex_to_decimal(hex_string):
    hex_chars = "0123456789ABCDEF"
    hex_string = hex_string.upper().lstrip("0X")
    if not hex_string:
        return 0

    def reducer(accumulator, char):
        digit_value = hex_chars.index(char)
        return accumulator * 16 + digit_value

    return reduce(reducer, hex_string, 0)

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("0X00FF"))
    print(hex_to_decimal("2F"))
    print(hex_to_decimal("0"))