def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1])
            compressed.append(str(count))
            count = 1
    compressed.append(s[-1])
    compressed.append(str(count))
    return "".join(compressed)

def solve(original_string):
    compressed = compress_string(original_string)
    if len(compressed) < len(original_string):
        return compressed
    return original_string

if __name__ == '__main__':
    test_cases = [
        "aabcccccaaa",
        "abcdef",
        "aabbcc",
        "aaaaaa",
        "",
        "a"
    ]
    for tc in test_cases:
        print(solve(tc))