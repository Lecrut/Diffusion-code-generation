import sys
from typing import List, Tuple

def decode_rle(compressed: str) -> str:
    if not compressed:
        return ""
    
    result_chars = []
    i = 0
    n = len(compressed)
    
    while i < n:
        if not compressed[i].isdigit():
            result_chars.append(compressed[i])
            i += 1
        else:
            num_start = i
            while i < n and compressed[i].isdigit():
                i += 1
            count = int(compressed[num_start:i])
            if i < n:
                char = compressed[i]
                result_chars.append(char * count)
                i += 1
    
    return "".join(result_chars)

if __name__ == '__main__':
    sample_input = "4a3b2c1d"
    decoded_output = decode_rle(sample_input)
    print(decoded_output)
    
    sample_large_input = "100a50b20c"
    decoded_large = decode_rle(sample_large_input)
    print(f"Length of large output: {len(decoded_large)}")
    print(decoded_large[:50])