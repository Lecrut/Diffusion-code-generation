import functools

def hex_to_decimal(hex_string):
    hex_chars = "0123456789ABCDEF"
    return functools.reduce(lambda acc, char: acc * 16 + hex_chars.index(char.upper()), hex_string, 0)

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)
    sample_hex_two = "FF"
    result_two = hex_to_decimal(sample_hex_two)
    print(result_two)