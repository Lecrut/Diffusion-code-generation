import itertools

def rle_compress(text):
    if not text:
        return ""
    result = []
    for key, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        result.append(f"{count}{key}")
    return "".join(result)

if __name__ == '__main__':
    sample = "AAABBBCCDDDEEEE"
    compressed = rle_compress(sample)
    print(compressed)