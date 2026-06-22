def compress_string(s: str) -> str:
    if not s:
        return s
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
    compressed_str = "".join(compressed)
    if len(compressed_str) < len(s):
        return compressed_str
    return s

if __name__ == '__main__':
    input_string = 'aabcccccaaa'
    result = compress_string(input_string)
    print(result)