def compress_string(s):
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
    result = "".join(compressed)
    if len(result) >= len(s):
        return s
    return result

if __name__ == '__main__':
    sample = 'aaaaabbcccd'
    print(compress_string(sample))