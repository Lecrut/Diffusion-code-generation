from typing import Union

def hex_to_decimal(hex_string: str) -> int:
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    
    is_negative = False
    working_string = hex_string
    
    if working_string.startswith('-'):
        is_negative = True
        working_string = working_string[1:]
    elif working_string.startswith('+'):
        working_string = working_string[1:]
    
    if not working_string:
        raise ValueError("Invalid hexadecimal format")
    
    result = 0
    multiplier = 1
    
    for char in reversed(working_string):
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit_value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit_value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        result += digit_value * multiplier
        multiplier *= 16
    
    if is_negative:
        result = -result
    
    return result

if __name__ == '__main__':
    sample_hex = "1A3F"
    calculated_decimal = hex_to_decimal(sample_hex)
    print(calculated_decimal)
    sample_hex_negative = "-1F"
    calculated_decimal_negative = hex_to_decimal(sample_hex_negative)
    print(calculated_decimal_negative)