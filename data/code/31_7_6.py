import functools
import string

def hex_string_to_decimal(hex_str):
    hex_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return functools.reduce(lambda acc, char: acc * 16 + hex_chars.index(char), hex_str, 0)

if __name__ == '__main__':
    sample_hex_values = ["1A", "FF", "10", "ABC"]
    for value in sample_hex_values:
        result = hex_string_to_decimal(value)
        print(f"{value} -> {result}")