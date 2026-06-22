from typing import Tuple

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded_parts: list[str] = []
    current_char: str = text[0]
    count: int = 1
    
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
    decoded_parts: list[str] = []
    i: int = 0
    n: int = len(text)
    
    while i < n:
        count_str: str = ""
        while i < n and text[i].isdigit():
            count_str += text[i]
            i += 1
        count: int = int(count_str)
        char: str = text[i]
        decoded_parts.append(char * count)
        i += 1
        
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_string: str = "AAABBBCCCCD"
    encoded: str = run_length_encode(sample_string)
    print(encoded)
    decoded: str = run_length_decode(encoded)
    print(decoded)