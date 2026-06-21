from typing import Final

def hex_to_decimal(hex_string: str) -> int:
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    
    is_negative = False
    if hex_string[0] == '-':
        is_negative = True
        hex_string = hex_string[1:]
    
    if not hex_string:
        raise ValueError("No digits provided after sign")
    
    result = 0
    base = 16
    
    for char in hex_string:
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        
        result = (result << 4) | value
    
    return -result if is_negative else result

if __name__ == '__main__':
    sample_input: Final[str] = "1A3F"
    computed_value: int = hex_to_decimal(sample_input)
    print(computed_value)