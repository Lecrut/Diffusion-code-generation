def encode_repeats(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(s[i - 1])
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(s[-1])
    return "".join(result)

if __name__ == '__main__':
    print(encode_repeats("aabbbc"))
    print(encode_repeats("abcd"))
    print(encode_repeats("aaa"))
    print(encode_repeats(""))
    print(encode_repeats("a"))