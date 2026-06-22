def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed.append(s[i - 1] + str(count))
            else:
                compressed.append(s[i - 1])
            count = 1
    if count > 1:
        compressed.append(s[-1] + str(count))
    else:
        compressed.append(s[-1])
    return "".join(compressed)

if __name__ == '__main__':
    print(compress_string("aabcccccaaa"))
    print(compress_string("abcdef"))
    print(compress_string("aabbcc"))
    print(compress_string(""))
    print(compress_string("z"))