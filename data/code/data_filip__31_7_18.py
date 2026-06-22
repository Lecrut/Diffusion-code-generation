import functools

def hex_to_decimal(hex_string):
    def accumulator(acc, char):
        return acc * 16 + int(char, 16)
    return functools.reduce(accumulator, hex_string, 0)

if __name__ == '__main__':
    result = hex_to_decimal("1A3F")
    print(result)