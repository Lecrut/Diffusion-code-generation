from functools import reduce

def hex_to_decimal(hex_string):
    return reduce(lambda acc, char: acc * 16 + int(char, 16), hex_string.upper(), 0)

if __name__ == '__main__':
    sample_hex_values = ["1A", "FF", "0", "10", "DEADBEEF"]
    for hex_val in sample_hex_values:
        decimal_val = hex_to_decimal(hex_val)
        print(decimal_val)