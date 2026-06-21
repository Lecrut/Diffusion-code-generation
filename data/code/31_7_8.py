from functools import reduce

def hex_to_decimal(hex_string):
    hex_chars = list(hex_string)
    
    def accumulator(acc, char):
        digit = int(char, 16)
        return acc * 16 + digit
    
    return reduce(accumulator, hex_chars, 0)

if __name__ == '__main__':
    result = hex_to_decimal("1A3F")
    print(result)