def compress_rle(data):
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
    return compressed

def decompress_rle(compressed):
    decompressed = []
    for char, count in compressed:
        decompressed.append(char * count)
    return "".join(decompressed)

def bidirectional_rle_verify(data):
    compressed = compress_rle(data)
    decompressed = decompress_rle(compressed)
    return compressed, decompressed, data == decompressed

if __name__ == '__main__':
    sample_data = "AAABBBCCD"
    compressed, decompressed, integrity = bidirectional_rle_verify(sample_data)
    print(compressed)
    print(decompressed)
    print(integrity)