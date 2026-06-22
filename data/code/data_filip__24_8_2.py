def rle_compress(data):
    if not data:
        return '', 0.0
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 9:
            count += 1
        else:
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
    compressed.append(f"{count}{current_char}")
    compressed_str = ''.join(compressed)
    ratio = len(compressed_str) / len(data)
    return compressed_str, ratio

def rle_decompress(compressed):
    decompressed = []
    i = 0
    while i < len(compressed):
        count = int(compressed[i])
        char = compressed[i + 1]
        decompressed.append(char * count)
        i += 2
    return ''.join(decompressed)

if __name__ == '__main__':
    sample_data = 'A' * 300 + 'B' * 200 + 'A' * 150 + 'C' * 250
    assert len(sample_data) == 900
    sample_data += 'D' * 100
    assert len(sample_data) == 1000
    compressed, ratio = rle_compress(sample_data)
    print(compressed)
    print(ratio)
    original = rle_decompress(compressed)
    assert original == sample_data