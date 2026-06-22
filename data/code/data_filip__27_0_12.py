def rle_encode(s):
    if not s:
        return []
    return [
        (s[i], s.count(s[i], i, next((j for j in range(i + 1, len(s) + 1) if j == len(s) or s[j] != s[i]), len(s))))
        for i in range(len(s))
        if i == 0 or s[i] != s[i - 1]
    ]

if __name__ == '__main__':
    sample1 = "AABCCCDEEEE"
    print(rle_encode(sample1))
    sample2 = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    print(rle_encode(sample2))
    sample3 = ""
    print(rle_encode(sample3))
    sample4 = "ABC"
    print(rle_encode(sample4))
    sample5 = "AAABBBCCC"
    print(rle_encode(sample5))