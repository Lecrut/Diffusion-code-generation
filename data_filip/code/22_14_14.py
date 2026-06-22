def compress_rle(s):
    if not s:
        return s
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1])
            if count > 1:
                compressed.append(str(count))
            count = 1
    compressed.append(s[-1])
    if count > 1:
        compressed.append(str(count))
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

if __name__ == '__main__':
    sample_inputs = [
        "aabcccccaaa",
        "abcd",
        "aaa",
        "aabb",
        "aabbbcccc",
        "abcde",
        "aaabbaaa",
        "hello"
    ]
    for s in sample_inputs:
        result = compress_rle(s)
        print(result)