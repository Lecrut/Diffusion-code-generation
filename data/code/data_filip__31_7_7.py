from functools import reduce

def hex_to_decimal(hex_str):
    def accumulator(acc, char):
        digit = int(char, 16)
        return acc * 16 + digit
    return reduce(accumulator, hex_str.lower().lstrip('0x'), 0)

if __name__ == '__main__':
    print(hex_to_decimal("1A"))
    print(hex_to_decimal("FF"))
    print(hex_to_decimal("0x10"))