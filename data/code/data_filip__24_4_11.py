import itertools

def compress_rle(s):
    if not s:
        return ""
    groups = itertools.groupby(s)
    compressed = []
    for key, group in groups:
        count = sum(1 for _ in group)
        compressed.append(f"{count}{key}")
    return "".join(compressed)

if __name__ == '__main__':
    sample = "AAABBBCCDAA"
    result = compress_rle(sample)
    print(result)