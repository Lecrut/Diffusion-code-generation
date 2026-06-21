def rle_compress(s):
    if not s:
        return ''

    result = []
    i = 0
    n = len(s)

    while i < n:
        current_char = s[i]
        count = 1
        while i + count < n and s[i + count] == current_char:
            count += 1

        if count >= 3:
            result.append(str(count) + current_char)
        else:
            result.append(current_char * count)

        i += count

    return ''.join(result)

if __name__ == '__main__':
    sample1 = "aaabbbccdd"
    sample2 = "aabbbcccc"
    sample3 = "abcdef"
    sample4 = "aaabbaaaccc"
    sample5 = ""
    sample6 = "a"
    sample7 = "aa"
    sample8 = "aaa"
    sample9 = "aaabbbcccddd"
    sample10 = "aabbbcc"

    print(rle_compress(sample1))
    print(rle_compress(sample2))
    print(rle_compress(sample3))
    print(rle_compress(sample4))
    print(rle_compress(sample5))
    print(rle_compress(sample6))
    print(rle_compress(sample7))
    print(rle_compress(sample8))
    print(rle_compress(sample9))
    print(rle_compress(sample10))