from typing import Optional

def hex_to_decimal(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise TypeError("Input must be a string")
    
    clean_string = hex_string.strip()
    if clean_string.startswith(('0x', '0X')):
        clean_string = clean_string[2:]
    elif clean_string.startswith(('-', '+')):
        prefix = clean_string[0]
        clean_string = clean_string[1:]
        if prefix == '-':
            return -int(clean_string, 16)
        elif prefix == '+':
            return int(clean_string, 16)
    
    if not clean_string:
        raise ValueError("Empty string provided")
    
    result = 0
    length = len(clean_string)
    
    for i, char in enumerate(clean_string):
        char = char.lower()
        value = 0
        
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        result = result * 16 + value
    
    return result

if __name__ == '__main__':
    sample_hex_1 = "1A"
    sample_hex_2 = "0xFF"
    sample_hex_3 = "-10"
    
    print(hex_to_decimal(sample_hex_1))
    print(hex_to_decimal(sample_hex_2))
    print(hex_to_decimal(sample_hex_3))