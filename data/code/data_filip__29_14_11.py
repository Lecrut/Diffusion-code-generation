def compress_string(s):
    if not s:
        return ""
    compressed = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(current_char)
                compressed.append(str(count))
            else:
                compressed.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        compressed.append(current_char)
        compressed.append(str(count))
    else:
        compressed.append(current_char)
    return "".join(compressed)

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    sample2 = "abc"
    sample3 = "aaabbbccc"
    sample4 = ""
    sample5 = "a"
    print(compress_string(sample1))
    print(compress_string(sample2))
    print(compress_string(sample3))
    print(compress_string(sample4))
    print(compress_string(sample5))