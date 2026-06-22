def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{count}{s[i - 1]}")
            count = 1
    compressed.append(f"{count}{s[-1]}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_input = 'cccccccccc'
    result = compress_string(sample_input)
    print(result)