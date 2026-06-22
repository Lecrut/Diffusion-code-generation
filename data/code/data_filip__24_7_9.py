def rle_compress(data):
    if not data:
        return ""
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1
    compressed.append((current_char, count))
    return ''.join(f"{char}{count}" for char, count in compressed)

def rle_decompress(compressed):
    if not compressed:
        return ""
    decompressed = []
    i = 0
    while i < len(compressed):
        char = compressed[i]
        i += 1
        count_str = ""
        while i < len(compressed) and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        if count_str:
            count = int(count_str)
        else:
            count = 1
        decompressed.append(char * count)
    return ''.join(decompressed)

if __name__ == '__main__':
    sample_data = "0011100"
    compressed = rle_compress(sample_data)
    print(compressed)
    decompressed = rle_decompress(compressed)
    print(decompressed)
    empty_compressed = rle_compress("")
    print(empty_compressed)
    empty_decompressed = rle_decompress("")
    print(empty_decompressed)
    single_char_compressed = rle_compress("1")
    print(single_char_compressed)
    single_char_decompressed = rle_decompress(single_char_compressed)
    print(single_char_decompressed)