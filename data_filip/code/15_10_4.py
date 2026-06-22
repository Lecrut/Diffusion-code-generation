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
    
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbbcc"
    sample2 = "abc"
    sample3 = "a"
    sample4 = ""
    sample5 = "aabcccccaaa"
    
    print(compress_string(sample1))
    print(compress_string(sample2))
    print(compress_string(sample3))
    print(compress_string(sample4))
    print(compress_string(sample5))