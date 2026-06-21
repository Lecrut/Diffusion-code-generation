def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1
    compressed.append(f"{s[-1]}{count}")
    return "".join(compressed)

def rle_optimized(s):
    compressed = compress_string(s)
    if len(compressed) < len(s):
        return compressed
    return s

if __name__ == "__main__":
    sample_strings = ["aabcccccaaa", "abcde", "aabbcc", ""]
    for text in sample_strings:
        result = rle_optimized(text)
        print(f"Input: '{text}' -> Output: '{result}'")