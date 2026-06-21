def compress_string(s):
    if not s:
        return ""

    compressed = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            compressed.append(str(count))
            current_char = s[i]
            count = 1

    compressed.append(current_char)
    compressed.append(str(count))

    return "".join(compressed)

if __name__ == '__main__':
    print(compress_string("aabbbcccc"))
    print(compress_string("abc"))
    print(compress_string("a"))
    print(compress_string(""))
    print(compress_string("aaaaa"))