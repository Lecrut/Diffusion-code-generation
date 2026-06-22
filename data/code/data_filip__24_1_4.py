def rle_decompress(compressed):
    if not compressed:
        return ''
    decompressed = []
    i = 0
    n = len(compressed)
    while i < n:
        count_str = ''
        while i < n and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        if not count_str:
            count = 1
        else:
            count = int(count_str)
        if i < n:
            char = compressed[i]
            i += 1
            decompressed.append(char * count)
        else:
            break
    return ''.join(decompressed)

if __name__ == '__main__':
    compressed_sample = '3A2B5C1A'
    result = rle_decompress(compressed_sample)
    print(result)

    compressed_empty = ''
    result_empty = rle_decompress(compressed_empty)
    print(result_empty)

    compressed_single = '1Z'
    result_single = rle_decompress(compressed_single)
    print(result_single)

    compressed_mixed = '10A1B0C'
    result_mixed = rle_decompress(compressed_mixed)
    print(result_mixed)