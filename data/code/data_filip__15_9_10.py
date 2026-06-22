from typing import List, Dict, Any, Tuple

def compress_string(input_str: str) -> str:
    if not input_str:
        return ""
    
    compressed_parts: List[str] = []
    current_char: str = input_str[0]
    count: int = 1
    
    for i in range(1, len(input_str)):
        char: str = input_str[i]
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(current_char)
            compressed_parts.append(str(count))
            current_char = char
            count = 1
    
    compressed_parts.append(current_char)
    compressed_parts.append(str(count))
    
    result: str = "".join(compressed_parts)
    
    if len(result) < len(input_str):
        return result
    return input_str

if __name__ == "__main__":
    sample_input: str = "aabcccccaaa"
    output: str = compress_string(sample_input)
    print(output)