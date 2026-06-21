def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = char
            count = 1
    
    compressed.append(current_char)
    compressed.append(str(count))
    
    compressed_str = "".join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

if __name__ == '__main__':
    test_input = 'aabcccccaaa'
    result = compress_string(test_input)
    print(result)