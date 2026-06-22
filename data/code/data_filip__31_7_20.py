import functools
import string

def hex_to_decimal(hex_str):
    hex_chars = string.hexdigits[:16].lower()
    char_map = {ch: i for i, ch in enumerate(hex_chars)}
    digits = [char_map[ch] for ch in hex_str]
    def acc(accum, value):
        return accum * 16 + value
    result = functools.reduce(acc, digits, 0)
    return result

if __name__ == '__main__':
    sample_hex = "1a3f"
    decimal_value = hex_to_decimal(sample_hex)
    print(decimal_value)