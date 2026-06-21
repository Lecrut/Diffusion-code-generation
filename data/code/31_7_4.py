import functools
import string

HEX_DIGITS = string.digits + 'abcdefABCDEF'

def hex_string_to_decimal(hex_string):
    def accumulator(acc, char):
        if char in string.digits:
            digit = int(char)
        elif char in string.ascii_lowercase:
            digit = 10 + string.ascii_lowercase.index(char)
        else:
            digit = 10 + string.ascii_uppercase.index(char)
        return acc * 16 + digit
    return functools.reduce(accumulator, hex_string, 0)

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_string_to_decimal(sample_hex)
    print(result)
    sample_hex2 = "FF"
    result2 = hex_string_to_decimal(sample_hex2)
    print(result2)