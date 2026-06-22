import re
from typing import List, Tuple

def compress(text: str) -> str:
    if not text:
        return ""
    
    chunks: List[Tuple[str, int]] = []
    current_char: str = text[0]
    count: int = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            chunks.append((current_char, count))
            current_char = char
            count = 1
    chunks.append((current_char, count))
    
    parts: List[str] = []
    for char, count in chunks:
        if count == 1:
            parts.append(char)
        else:
            parts.append(f"{char}{count}")
    return "".join(parts)

def decompress(text: str) -> str:
    if not text:
        return ""
    
    result: List[str] = []
    current_num_str: str = ""
    
    for char in text:
        if char.isdigit():
            current_num_str += char
        else:
            if current_num_str:
                count = int(current_num_str)
                result.append(char * count)
                current_num_str = ""
            else:
                result.append(char)
                
    if current_num_str:
        count = int(current_num_str)
        result.append(char * count)
        
    return "".join(result)

if __name__ == '__main__':
    sample_text: str = "aaabbcccccc"
    compressed: str = compress(sample_text)
    print(compressed)
    
    decompressed: str = decompress(compressed)
    print(decompressed)