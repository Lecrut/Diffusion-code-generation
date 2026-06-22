import io
import itertools
import re

def rle_compression(data):
    if not data:
        return ""
    compressed_parts = []
    for key, group in itertools.groupby(data):
        count = len(list(group))
        if count == 1:
            compressed_parts.append(key)
        else:
            compressed_parts.append(str(count) + key)
    return "".join(compressed_parts)

def rle_decompression(data):
    if not data:
        return ""
    pattern = re.compile(r'(\d+)?([a-zA-Z0-9])')
    decompressed_parts = []
    for match in pattern.finditer(data):
        count_str = match.group(1)
        char = match.group(2)
        if count_str:
            decompressed_parts.append(char * int(count_str))
        else:
            decompressed_parts.append(char)
    return "".join(decompressed_parts)

if __name__ == '__main__':
    original_string = "aabcccccaaa"
    compressed = rle_compression(original_string)
    decompressed = rle_decompression(compressed)
    print(decompressed)