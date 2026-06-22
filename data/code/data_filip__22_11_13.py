import re
from typing import List

def decompress_rle(encoded: str) -> str:
    pattern = re.compile(r'(\D)(\d+)')
    parts: List[str] = []
    
    for match in pattern.finditer(encoded):
        char: str = match.group(1)
        count: int = int(match.group(2))
        parts.append(char * count)
        
    return "".join(parts)

if __name__ == '__main__':
    sample_input = "a3b4c2"
    result = decompress_rle(sample_input)
    print(result)