import itertools

def rle_compress(data: str) -> str:
    compressed = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        compressed.append(f"{count}{key}")
    return "".join(compressed)

def rle_decompress(data: str) -> str:
    decompressed = []
    i = 0
    length = len(data)
    while i < length:
        count_str = []
        while i < length and data[i].isdigit():
            count_str.append(data[i])
            i += 1
        count = int("".join(count_str))
        if i < length:
            char = data[i]
            decompressed.append(char * count)
            i += 1
    return "".join(decompressed)

if __name__ == '__main__':
    original = "AAABBBCCDAA"
    compressed = rle_compress(original)
    decompressed = rle_decompress(compressed)
    print(decompressed)