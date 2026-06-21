def encode_consecutive_duplicates(s):
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
            result.append(str(count))
            current_char = s[i]
            count = 1
    
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

if __name__ == '__main__':
    print(encode_consecutive_duplicates("aaabbc"))
    print(encode_consecutive_duplicates("hello"))
    print(encode_consecutive_duplicates("a"))
    print(encode_consecutive_duplicates(""))
    print(encode_consecutive_duplicates("aabcc"))