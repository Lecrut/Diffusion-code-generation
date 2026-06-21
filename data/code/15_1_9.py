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
    result = "".join(compressed)
    if len(result) < len(s):
        return result
    return s

if __name__ == '__main__':
    sample = 'aaaaabbbbcccd'
    print(compress_string(sample))