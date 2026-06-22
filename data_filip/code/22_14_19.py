def compress_string(s: str) -> str:
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

def solve(original: str) -> str:
    compressed = compress_string(original)
    if len(compressed) < len(original):
        return compressed
    return original

if __name__ == '__main__':
    print(solve("aabcccccaaa"))
    print(solve("abc"))
    print(solve("aaa"))