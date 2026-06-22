def compress_string(s):
    if not s:
        return ''
    
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
    
    result = ''.join(compressed)
    return result if len(result) < len(s) else s

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    sample2 = "abcd"
    sample3 = "aaaaa"
    sample4 = ""
    sample5 = "a"
    
    print(compress_string(sample1))
    print(compress_string(sample2))
    print(compress_string(sample3))
    print(compress_string(sample4))
    print(compress_string(sample5))