from typing import Tuple

def compress_string(s: str) -> str:
    if not s:
        return s
    
    compressed_parts: list[Tuple[str, int]] = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed_parts.append((current_char, count))
            current_char = s[i]
            count = 1
    
    compressed_parts.append((current_char, count))
    
    result = "".join(f"{char}{count}" for char, count in compressed_parts)
    
    if len(result) < len(s):
        return result
    return s

if __name__ == '__main__':
    sample_input = 'aabcccccaaa'
    result = compress_string(sample_input)
    print(result)