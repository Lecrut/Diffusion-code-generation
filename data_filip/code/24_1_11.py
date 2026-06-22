def rle_decompress(compressed):
    if not compressed:
        return ""
    original = []
    i = 0
    n = len(compressed)
    while i < n:
        char = compressed[i]
        i += 1
        count_str = ""
        while i < n and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        if count_str:
            count = int(count_str)
        else:
            count = 1
        original.append(char * count)
    return "".join(original)

if __name__ == '__main__':
    compressed_samples = [
        "A3B2C1",
        "abc",
        "x12y5",
        "",
        "Z1",
        "a0b3"
    ]
    for sample in compressed_samples:
        decompressed = rle_decompress(sample)
        print(decompressed)