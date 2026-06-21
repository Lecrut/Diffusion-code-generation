def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char)
    compressed.append(str(count))
    
    result = "".join(compressed)
    
    if len(result) >= len(s):
        return s
    
    return result

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = compress_string(sample_input)
    print(result)
    
    sample_input2 = "abcde"
    result2 = compress_string(sample_input2)
    print(result2)
    
    sample_input3 = ""
    result3 = compress_string(sample_input3)
    print(result3)
    
    sample_input4 = "aaabbcc"
    result4 = compress_string(sample_input4)
    print(result4)