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

def compare_lengths(original):
    compressed = compress_string(original)
    if len(compressed) < len(original):
        return compressed
    return original

if __name__ == '__main__':
    sample = "AAABBBCCDDD"
    result = compare_lengths(sample)
    print(result)