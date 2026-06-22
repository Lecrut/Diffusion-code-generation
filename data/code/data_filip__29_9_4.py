def encode_repeated_elements(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1
    result.append(s[-1])
    if count > 1:
        result.append(str(count))
    return "".join(result)

if __name__ == '__main__':
    print(encode_repeated_elements("aabbbc"))
    print(encode_repeated_elements("abc"))
    print(encode_repeated_elements("aabb"))
    print(encode_repeated_elements(""))
    print(encode_repeated_elements("aaaa"))