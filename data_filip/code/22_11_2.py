import re
import functools
import operator

def decompress_rle(compressed: str) -> str:
    if not compressed:
        return ""

    pattern = re.compile(r'([a-zA-Z])(\d+)')
    matches = pattern.findall(compressed)

    if not matches:
        return ""

    decompressed_chars = []
    for char, count_str in matches:
        count = int(count_str)
        decompressed_chars.append(char * count)

    return "".join(decompressed_chars)

if __name__ == '__main__':
    sample_compressed = "a1b2c3"
    result = decompress_rle(sample_compressed)
    print(result)

    sample_compressed2 = "h1e1l2o1"
    result2 = decompress_rle(sample_compressed2)
    print(result2)

    sample_compressed3 = "x10y2z1"
    result3 = decompress_rle(sample_compressed3)
    print(result3)