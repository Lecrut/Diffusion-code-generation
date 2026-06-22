import re
from typing import Tuple

def compress_text(text: str) -> str:
    if not text:
        return ""
    
    result = []
    run_length = 1
    text_length = len(text)
    
    for i in range(1, text_length):
        if text[i] == text[i - 1]:
            run_length += 1
        else:
            if run_length > 1:
                result.append(f"{run_length}{text[i - 1]}")
            else:
                result.append(text[i - 1])
            run_length = 1
    
    if run_length > 1:
        result.append(f"{run_length}{text[-1]}")
    else:
        result.append(text[-1])
    
    return "".join(result)

def decompress_text(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    number_str = []
    
    for char in compressed:
        if char.isdigit():
            number_str.append(char)
        else:
            if number_str:
                count = int("".join(number_str))
                result.append(char * count)
                number_str = []
            else:
                result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    original = "AAAABBBCCDAA"
    compressed = compress_text(original)
    decompressed = decompress_text(compressed)
    
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Matches: {original == decompressed}")