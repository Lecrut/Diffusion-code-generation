import itertools

def rle_compress(s):
    if not s:
        return []
    compressed = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        compressed.append((char, count))
    return compressed

def rle_decompress(compressed):
    return ''.join(char * count for char, count in compressed)

if __name__ == '__main__':
    sample_string = "aaabbbccccdd"
    compressed_data = rle_compress(sample_string)
    decompressed_data = rle_decompress(compressed_data)
    print(f"Original: {sample_string}")
    print(f"Compressed: {compressed_data}")
    print(f"Decompressed: {decompressed_data}")