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
            compressed.append(current_char)
            if count > 1:
                compressed.append(str(count))
            current_char = s[i]
            count = 1
    
    compressed.append(current_char)
    if count > 1:
        compressed.append(str(count))
    
    compressed_str = "".join(compressed)
    
    if len(compressed_str) < len(s):
        return compressed_str
    else:
        return s

if __name__ == '__main__':
    print(compress_string("aaabbcccc"))
    print(compress_string("abcdef"))
    print(compress_string("aabbc"))
    print(compress_string(""))
    print(compress_string("a"))