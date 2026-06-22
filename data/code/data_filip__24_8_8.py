def rle_compress(data):
    if not data:
        return "", 0.0
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 9:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    compressed_str = "".join(compressed)
    ratio = len(data) / len(compressed_str) if len(compressed_str) > 0 else 0.0
    return compressed_str, ratio

if __name__ == '__main__':
    test_string = "A" * 300 + "B" * 200 + "C" * 150 + "D" * 100 + "E" * 250
    compressed_data, compression_ratio = rle_compress(test_string)
    print(compressed_data)
    print(compression_ratio)