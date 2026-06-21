from typing import Tuple, Optional

def compress_string(input_string: str) -> Optional[str]:
    if not input_string:
        return input_string
    
    compressed_parts: list[Tuple[str, int]] = []
    current_char: str = input_string[0]
    count: int = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed_parts.append((current_char, count))
            current_char = char
            count = 1
    
    compressed_parts.append((current_char, count))
    
    compressed_list: list[str] = []
    for char, count in compressed_parts:
        compressed_list.append(f"{char}{count}")
    
    compressed_result: str = "".join(compressed_list)
    
    if len(compressed_result) < len(input_string):
        return compressed_result
    
    return None

if __name__ == '__main__':
    sample_input = 'aabcccccaaa'
    result = compress_string(sample_input)
    print(result if result is not None else sample_input)