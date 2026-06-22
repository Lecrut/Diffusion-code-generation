import itertools

def compress_rle(data):
    if not data:
        return []
    compressed = []
    for char, group in itertools.groupby(data):
        count = len(list(group))
        compressed.append((char, count))
    return compressed

def decompress_rle(compressed_data):
    return ''.join(char * count for char, count in compressed_data)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDEEEFFF"
    compressed_result = compress_rle(sample_string)
    decompressed_result = decompress_rle(compressed_result)
    print(compressed_result)
    print(decompressed_result)