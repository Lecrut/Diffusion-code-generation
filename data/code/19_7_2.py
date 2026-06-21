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
    return compressed

def rle_decompress(compressed):
    decompressed = []
    for char, count in compressed:
        decompressed.append(char * count)
    return "".join(decompressed)

def bidirectional_rle(data):
    compressed = rle_compress(data)
    decompressed = rle_decompress(compressed)
    return compressed, decompressed

if __name__ == "__main__":
    sample_data = "AAABBBCCCCCDDEEE"
    compressed, decompressed = bidirectional_rle(sample_data)
    print(compressed)
    print(decompressed)