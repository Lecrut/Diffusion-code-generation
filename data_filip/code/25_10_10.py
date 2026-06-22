def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(str(count))
            compressed.append(current_char)
            current_char = s[i]
            count = 1
    
    compressed.append(str(count))
    compressed.append(current_char)
    
    result = ''.join(compressed)
    if len(result) < len(s):
        return result
    else:
        return s

if __name__ == '__main__':
    print(compress_string(""))
    print(compress_string("a"))
    print(compress_string("aabcccccaaa"))
    print(compress_string("abcdef"))
    print(compress_string("aaabbbcc"))
    print(compress_string("aabbbbcccccc"))