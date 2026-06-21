import functools

def hex_to_decimal(hex_string):
    hex_string = hex_string.lower()
    def accumulator(value, char):
        if char in '0123456789':
            digit = ord(char) - 48
        elif char in 'abcdef':
            digit = ord(char) - 87
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        return value * 16 + digit
    return functools.reduce(accumulator, hex_string, 0)

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)
    sample_hex2 = "FF"
    result2 = hex_to_decimal(sample_hex2)
    print(result2)