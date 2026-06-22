def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    print(compress_string("aabcccccaaa"))
    print(compress_string("abcdef"))
    print(compress_string("aabb"))
    print(compress_string(""))
    print(compress_string("aaaaa"))
    print(compress_string("a"))