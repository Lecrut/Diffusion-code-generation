def compress_string(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    
    compressed = "".join(result)
    if len(compressed) < len(s):
        return compressed
    return s

if __name__ == "__main__":
    print(compress_string("aabcccccaaa"))
    print(compress_string("abc"))
    print(compress_string("aabbcc"))
    print(compress_string(""))
    print(compress_string("a"))
    print(compress_string("aa"))