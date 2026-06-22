import re

def rle_compress(s):
    if not s:
        return ""
    compressed = []
    i = 0
    while i < len(s):
        char = s[i]
        count = 1
        while i + count < len(s) and s[i + count] == char:
            count += 1
        if count > 1:
            compressed.append(str(count) + char)
        else:
            compressed.append(char)
        i += count
    return "".join(compressed)

def rle_decompress(s):
    if not s:
        return ""
    decompressed = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num_str = []
            while i < len(s) and s[i].isdigit():
                num_str.append(s[i])
                i += 1
            count = int("".join(num_str))
            char = s[i]
            decompressed.append(char * count)
            i += 1
        else:
            decompressed.append(s[i])
            i += 1
    return "".join(decompressed)

def compress_and_decompress(input_str):
    compressed = rle_compress(input_str)
    decompressed = rle_decompress(compressed)
    return decompressed

if __name__ == '__main__':
    sample_string = "AAABBBCCCD"
    result = compress_and_decompress(sample_string)
    print(result)