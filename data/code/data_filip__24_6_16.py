import re

def rle_roundtrip(s):
    compressed = re.sub(r'(.)\1+', lambda m: f"{len(m.group(0))}{m.group(1)}", s)
    decompressed = re.sub(r'(\d+)(.)', lambda m: m.group(2) * int(m.group(1)), compressed)
    return compressed, decompressed

if __name__ == '__main__':
    sample = "AAABBBCCCDAA"
    compressed, decompressed = rle_roundtrip(sample)
    print(compressed)
    print(decompressed)