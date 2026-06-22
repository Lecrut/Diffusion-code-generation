def encode_repeated_elements(s):
    if not s:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(s[i - 1] + str(count))
            else:
                result.append(s[i - 1])
            count = 1
    
    if count > 1:
        result.append(s[-1] + str(count))
    else:
        result.append(s[-1])
    
    return "".join(result)

if __name__ == '__main__':
    print(encode_repeated_elements("aabbbc"))
    print(encode_repeated_elements("hello"))
    print(encode_repeated_elements("aaabbbccc"))
    print(encode_repeated_elements("abcd"))
    print(encode_repeated_elements(""))