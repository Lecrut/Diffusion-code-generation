def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    length = len(s)
    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            result.append(str(count))
            count = 1
    result.append(s[length - 1])
    result.append(str(count))
    compressed = "".join(result)
    if len(compressed) >= len(s):
        return s
    return compressed

if __name__ == "__main__":
    sample_input_1 = "aaabbbcccaaa"
    sample_input_2 = "abcd"
    sample_input_3 = "aaaa"
    print(compress_string(sample_input_1))
    print(compress_string(sample_input_2))
    print(compress_string(sample_input_3))