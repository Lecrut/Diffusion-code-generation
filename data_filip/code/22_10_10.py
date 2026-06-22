def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char + str(count))
    
    result = "".join(compressed)
    
    if len(result) < len(s):
        return result
    return s

if __name__ == '__main__':
    test_string = "aabcccccaaa"
    compressed_result = compress_string(test_string)
    print(compressed_result)