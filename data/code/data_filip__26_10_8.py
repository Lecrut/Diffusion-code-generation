def rle_encode(s):
    if not s:
        return ""
    result = []
    i = 0
    n = len(s)
    while i < n:
        char = s[i]
        count = 1
        j = i + 1
        while j < n and s[j] == char:
            count += 1
            j += 1
        result.append(f"{count}{char}")
        i = j
    return "".join(result)

if __name__ == '__main__':
    sample1 = "aaabbbcc"
    sample2 = "abcd"
    sample3 = "wwwwwaaaaaaasssssss"
    print(rle_encode(sample1))
    print(rle_encode(sample2))
    print(rle_encode(sample3))