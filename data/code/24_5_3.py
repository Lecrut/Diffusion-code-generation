import re
from typing import Tuple

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded_parts = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded_parts.append(f"{count}{current_char}")
    
    return "".join(encoded_parts)

def run_length_decode(text: str) -> str:
    if not text:
        return ""
    
    decoded_chars = []
    count_str = []
    
    for char in text:
        if char.isdigit():
            count_str.append(char)
        else:
            count = int("".join(count_str))
            decoded_chars.append(char * count)
            count_str = []
    
    return "".join(decoded_chars)

if __name__ == '__main__':
    original_string = "AAABBBCCDDA"
    
    encoded_string = run_length_encode(original_string)
    print(f"Encoded: {encoded_string}")
    
    decoded_string = run_length_decode(encoded_string)
    print(f"Decoded: {decoded_string}")