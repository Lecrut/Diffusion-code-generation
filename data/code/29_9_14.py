def encode_repeated_elements(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(current_char)
                result.append(str(count))
            else:
                result.append(current_char)
            current_char = s[i]
            count = 1
    if count > 1:
        result.append(current_char)
        result.append(str(count))
    else:
        result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aabbbc"
    print(encode_repeated_elements(sample1))
    sample2 = "hello"
    print(encode_repeated_elements(sample2))
    sample3 = "aaabbbcc"
    print(encode_repeated_elements(sample3))
    sample4 = ""
    print(encode_repeated_elements(sample4))
    sample5 = "a"
    print(encode_repeated_elements(sample5))
    sample6 = "abcdef"
    print(encode_repeated_elements(sample6))
    sample7 = "aabbccddeeff"
    print(encode_repeated_elements(sample7))