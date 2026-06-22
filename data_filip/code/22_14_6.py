def compress_rle(s):
    if not s:
        return s
    result = []
    current = s[0]
    count = 1
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            result.append(f"{current}{count}")
            current = char
            count = 1
    result.append(f"{current}{count}")
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s

if __name__ == '__main__':
    sample1 = "aabcccccaaa"
    sample2 = "abc"
    sample3 = ""
    sample4 = "aaaaaaaaaa"
    print(compress_rle(sample1))
    print(compress_rle(sample2))
    print(compress_rle(sample3))
    print(compress_rle(sample4))