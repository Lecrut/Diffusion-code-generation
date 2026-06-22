def compress_rle(s: str) -> str:
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return "".join(compressed)

def rle_comparison(s: str) -> str:
    compressed = compress_rle(s)
    if len(compressed) < len(s):
        return compressed
    return s

if __name__ == '__main__':
    sample_strings = ["aaabbcccc", "abcde", "aabb", "", "aaaaaaaaaa"]
    for text in sample_strings:
        print(rle_comparison(text))