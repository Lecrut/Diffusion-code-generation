def encode_repeated_elements(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
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
    print(encode_repeated_elements("aabbc"))
    print(encode_repeated_elements("hello"))
    print(encode_repeated_elements("aaaa"))
    print(encode_repeated_elements("ab"))
    print(encode_repeated_elements(""))