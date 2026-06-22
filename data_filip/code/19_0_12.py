def compress_rle(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count) if count > 1 else s[i - 1])
            count = 1
    result.append(s[-1] + str(count) if count > 1 else s[-1])
    return "".join(result)

if __name__ == '__main__':
    print(compress_rle("aabcccccaaa"))
    print(compress_rle("abcdef"))
    print(compress_rle("AAAABBBCCD"))
    print(compress_rle(""))
    print(compress_rle("A"))
    print(compress_rle("AA"))
    print(compress_rle("AABBBCCCC"))