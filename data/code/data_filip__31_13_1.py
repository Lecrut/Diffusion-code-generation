from typing import Optional

def hex_to_decimal(hex_string: str) -> int:
    if not hex_string:
        return 0
    
    is_negative = False
    if hex_string.startswith('-'):
        is_negative = True
        hex_string = hex_string[1:]
    elif hex_string.startswith('+'):
        hex_string = hex_string[1:]
    
    result = 0
    shift = 0
    base = 16
    
    for char in reversed(hex_string):
        digit_value = 0
        code = ord(char)
        if 48 <= code <= 57:
            digit_value = code - 48
        elif 97 <= code <= 102:
            digit_value = code - 87
        elif 65 <= code <= 70:
            digit_value = code - 55
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        result += digit_value * (base ** shift)
        shift += 1
    
    return -result if is_negative else result

if __name__ == '__main__':
    sample_hex = "1A3F"
    print(hex_to_decimal(sample_hex))