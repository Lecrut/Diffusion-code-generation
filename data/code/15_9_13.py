def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 0
    
    for char in s:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = char
            count = 1
    compressed.append(current_char + str(count))
    
    result = "".join(compressed)
    return result if len(result) < len(s) else s

if __name__ == '__main__':
    original = 'aabcccccaaa'
    result = compress_string(original)
    print(result)