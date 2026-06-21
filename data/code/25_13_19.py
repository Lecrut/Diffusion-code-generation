import sys
from typing import List, Tuple, Any

def run_length_encode(data: str) -> List[Tuple[str, int]]:
    if not data:
        return []
    
    result: List[Tuple[str, int]] = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    return result

def run_length_decode(encoded_data: List[Tuple[str, int]]) -> str:
    if not encoded_data:
        return ""
    
    return "".join(char * count for char, count in encoded_data)

if __name__ == '__main__':
    sample_input = "aaabbccccddddd"
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    
    large_string = "a" * 10000 + "b" * 5000 + "c" * 2000
    large_encoded = run_length_encode(large_string)
    print(large_encoded)
    large_decoded = run_length_decode(large_encoded)
    print(len(large_decoded) == len(large_string))