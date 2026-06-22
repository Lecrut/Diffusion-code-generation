def rle_compress(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbbcc"
    sample2 = "abc"
    sample3 = "aaaaabbbbbccccc"
    sample4 = ""
    sample5 = "a"
    print(rle_compress(sample1))
    print(rle_compress(sample2))
    print(rle_compress(sample3))
    print(rle_compress(sample4))
    print(rle_compress(sample5))