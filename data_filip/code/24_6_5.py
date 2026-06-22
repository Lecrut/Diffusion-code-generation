import itertools

def rle_compress_decompress(s):
    compressed = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        compressed.append((char, count))
    decompressed = ''.join(char * count for char, count in compressed)
    return compressed, decompressed

if __name__ == '__main__':
    sample = "AAABBBCCD"
    result = rle_compress_decompress(sample)
    print(result)