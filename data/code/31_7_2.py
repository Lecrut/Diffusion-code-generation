import functools
import string

def hex_to_decimal(hex_str):
    valid_hex = string.hexdigits
    hex_chars = hex_str.lower()
    
    if not all(c in valid_hex for c in hex_chars):
        raise ValueError("Invalid hexadecimal string")
        
    if not hex_str:
        return 0
        
    digit_values = {c: i for i, c in enumerate(string.hexdigits[:16])}
    
    result = functools.reduce(
        lambda acc, char: acc * 16 + digit_values[char],
        hex_chars,
        0
    )
    
    return result

if __name__ == '__main__':
    hex_string = "1a3f"
    decimal_value = hex_to_decimal(hex_string)
    print(decimal_value)