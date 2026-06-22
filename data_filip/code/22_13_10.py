import sys
from typing import Iterator, Tuple, List, Union

def rle_compress_tight(data: str) -> str:
    if not data:
        return ""
    
    result: List[str] = []
    length = len(data)
    i = 0
    
    while i < length:
        char = data[i]
        count = 1
        while i + count < length and data[i + count] == char:
            count += 1
        
        if count >= 3:
            result.append(f"{char}{count}")
        elif count == 2:
            result.append(f"{char}{char}")
        else:
            result.append(char)
        
        i += count
    
    return "".join(result)

def rle_decompress_tight(compressed: str) -> str:
    if not compressed:
        return ""
    
    result: List[str] = []
    i = 0
    length = len(compressed)
    
    while i < length:
        char = compressed[i]
        i += 1
        if i < length and compressed[i].isdigit():
            num_str = ""
            while i < length and compressed[i].isdigit():
                num_str += compressed[i]
                i += 1
            count = int(num_str)
            if count >= 3:
                result.append(char * count)
            else:
                result.append(char * count)
        else:
            result.append(char)
    
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccdddeeeffgggghhiiijjjjj"
    compressed_output = rle_compress_tight(sample_input)
    decompressed_output = rle_decompress_tight(compressed_output)
    print(f"Original: {sample_input}")
    print(f"Compressed: {compressed_output}")
    print(f"Decompressed: {decompressed_output}")
    print(f"Round-trip match: {sample_input == decompressed_output}")