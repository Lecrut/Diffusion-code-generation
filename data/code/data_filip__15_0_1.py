def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    current_char = s[0]
    
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
    
    compressed_str = "".join(compressed)
    if len(compressed_str) < len(s):
        return compressed_str
    return s

if __name__ == '__main__':
    input_str = "aabcccccaaa"
    result = compress_string(input_str)
    print(result)