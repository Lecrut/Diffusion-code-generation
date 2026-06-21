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
            if count > 1:
                compressed.append(current_char)
                compressed.append(str(count))
            else:
                compressed.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        compressed.append(current_char)
        compressed.append(str(count))
    else:
        compressed.append(current_char)
    
    compressed_str = "".join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

if __name__ == '__main__':
    print(compress_string("aabcccccaaa"))
    print(compress_string("abcdef"))
    print(compress_string("aabbcc"))
    print(compress_string(""))
    print(compress_string("a"))
    print(compress_string("aaaaa"))