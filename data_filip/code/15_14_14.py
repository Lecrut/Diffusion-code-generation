def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    result = "".join(compressed)
    return result if len(result) < len(s) else s

if __name__ == '__main__':
    print(compress_string("aabcccccaaa"))
    print(compress_string("abcdef"))
    print(compress_string("a"))
    print(compress_string("aa"))
    print(compress_string("aabbbcccc"))