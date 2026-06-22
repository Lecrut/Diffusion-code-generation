def compress_rle(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(current_char)
                result.append(str(count))
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(current_char)
        result.append(str(count))
    else:
        result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    print(compress_rle("aabcccccaaa"))
    print(compress_rle("abc"))
    print(compress_rle("aaabbbcc"))
    print(compress_rle("a"))
    print(compress_rle(""))
    print(compress_rle("aaa"))
    print(compress_rle("aabcccccaaa"))