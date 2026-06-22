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
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    result.append(f"{current_char}{count}")
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    sample2 = "abcdef"
    sample3 = ""
    sample4 = "a"
    sample5 = "aaaabbbbcccc"
    print(compress_string(sample1))
    print(compress_string(sample2))
    print(compress_string(sample3))
    print(compress_string(sample4))
    print(compress_string(sample5))