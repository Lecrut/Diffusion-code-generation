def compress_string(s):
    if not s:
        return ""

    result = []
    count = 1
    current_char = s[0]

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = s[i]
            count = 1

    result.append(current_char)
    result.append(str(count))

    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    print(compress_string("aabcccccaaa"))
    print(compress_string("abc"))
    print(compress_string(""))
    print(compress_string("a"))
    print(compress_string("aaa"))
    print(compress_string("aabb"))
    print(compress_string("xyzzz"))