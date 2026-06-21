def compress_string(s):
    if not s:
        return s
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return ''.join(compressed)

def solve(original):
    if not original:
        return original
    compressed = compress_string(original)
    if len(compressed) < len(original):
        return compressed
    return original

if __name__ == '__main__':
    print(solve("aabcccccaaa"))
    print(solve("abcdef"))