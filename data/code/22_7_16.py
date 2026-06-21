import re
import itertools
import time

def rle_decode(compressed_string):
    if not compressed_string:
        return ""
    
    def decode_pair(pair):
        count = int(pair[0])
        char = pair[1]
        return char * count
    
    parts = []
    i = 0
    n = len(compressed_string)
    
    while i < n:
        if compressed_string[i].isdigit():
            end = i
            while end < n and compressed_string[end].isdigit():
                end += 1
            count = int(compressed_string[i:end])
            char = compressed_string[end]
            parts.append(char * count)
            i = end + 1
        else:
            parts.append(compressed_string[i])
            i += 1
    
    return "".join(parts)

if __name__ == '__main__':
    samples = [
        ("2h3e4l1l2o", "hheelllloo"),
        ("10a5b", "aaaaaaaaaabbbbb"),
        ("1z", "z"),
        ("", ""),
        ("3A1B2C", "AAABCC"),
    ]
    
    for compressed, expected in samples:
        result = rle_decode(compressed)
        print(f"Input: {compressed!r}, Output: {result!r}, Expected: {expected!r}, Pass: {result == expected}")
    
    large_input = "1000000a"
    start = time.time()
    result = rle_decode(large_input)
    elapsed = time.time() - start
    print(f"Large input test: len={len(result)}, time={elapsed:.4f}s")