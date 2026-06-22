def compress_string(s):
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
    sample_inputs = [
        "aabcccccaaa",
        "abcdef",
        "AAAAAAAA",
        "a",
        "",
        "aaabbbccc",
        "xyyz"
    ]
    for sample in sample_inputs:
        print(compress_string(sample))