def rle_compress(data):
    if not data:
        return ''
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = char
            count = 1
    compressed.append(str(count) + current_char)
    return ''.join(compressed)

def rle_decompress(compressed):
    if not compressed:
        return ''
    decompressed = []
    i = 0
    while i < len(compressed):
        count = int(compressed[i])
        i += 1
        char = compressed[i]
        decompressed.append(char * count)
        i += 1
    return ''.join(decompressed)

if __name__ == '__main__':
    sample_data = '0011100'
    compressed = rle_compress(sample_data)
    print(compressed)
    decompressed = rle_decompress(compressed)
    print(decompressed)
    empty_data = ''
    compressed_empty = rle_compress(empty_data)
    print(compressed_empty)
    decompressed_empty = rle_decompress(compressed_empty)
    print(decompressed_empty)
    single_char = 'A'
    compressed_single = rle_compress(single_char)
    print(compressed_single)
    decompressed_single = rle_decompress(compressed_single)
    print(decompressed_single)