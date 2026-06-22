def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed_parts = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(current_char + str(count))
            current_char = char
            count = 1
    
    compressed_parts.append(current_char + str(count))
    compressed_str = "".join(compressed_parts)
    
    if len(compressed_str) < len(s):
        return compressed_str
    else:
        return s

if __name__ == '__main__':
    result = compress_string('aabcccccaaa')
    print(result)