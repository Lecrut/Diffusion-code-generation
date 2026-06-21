import itertools
from collections import deque

def rle_compress_decompress(s):
    compressed = rle_compress(s)
    decompressed = rle_decompress(compressed)
    return decompressed

def rle_compress(s):
    if not s:
        return ""
    result = []
    groups = itertools.groupby(s)
    for char, group in groups:
        count = sum(1 for _ in group)
        result.append(f"{count}{char}")
    return "".join(result)

def rle_decompressed(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if count_str:
            count = int(count_str)
            char = s[i] if i < len(s) else ""
            result.append(char * count)
            i += 1
        else:
            break
    return "".join(result)

def rle_decompress(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if count_str:
            count = int(count_str)
            if i < len(s):
                char = s[i]
                result.append(char * count)
                i += 1
            else:
                break
        else:
            break
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    result = rle_compress_decompress(sample_string)
    print(result)