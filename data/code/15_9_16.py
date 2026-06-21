from typing import Optional

def compress_string(s: str) -> Optional[str]:
    if not s:
        return ""
    
    compressed_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed_parts.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    compressed_parts.append(f"{current_char}{count}")
    compressed = "".join(compressed_parts)
    
    if len(compressed) < len(s):
        return compressed
    return None

if __name__ == "__main__":
    input_str = "aabcccccaaa"
    result = compress_string(input_str)
    print(result)