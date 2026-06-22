def compress_rle(s):
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
                result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1

    if count > 1:
        result.append(str(count))
    result.append(current_char)

    return "".join(result)

if __name__ == '__main__':
    sample1 = "AAABBBCCD"
    sample2 = "ABC"
    sample3 = "AAAAAAAAAA"
    sample4 = ""
    sample5 = "A"

    print(compress_rle(sample1))
    print(compress_rle(sample2))
    print(compress_rle(sample3))
    print(compress_rle(sample4))
    print(compress_rle(sample5))