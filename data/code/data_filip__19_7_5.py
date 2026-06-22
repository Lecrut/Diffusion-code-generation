def compress_rle(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(str(count) + s[i - 1])
            count = 1
    compressed.append(str(count) + s[-1])
    return "".join(compressed)

def decompress_rle(s):
    if not s:
        return ""
    decompressed = []
    count = 0
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            decompressed.append(char * count)
            count = 0
    return "".join(decompressed)

def bidirectional_rle(s):
    compressed = compress_rle(s)
    decompressed = decompress_rle(compressed)
    return compressed, decompressed

if __name__ == '__main__':
    sample_input = "AAABBBCCDDDD"
    result = bidirectional_rle(sample_input)
    print(result)