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
            compressed.append(f"{count}{current_char}")
            current_char = char
            count = 1
    compressed.append(f"{count}{current_char}")
    compressed_string = "".join(compressed)
    ratio = len(compressed_string) / len(data)
    return compressed_string, ratio

if __name__ == '__main__':
    sample_data = "A" * 500 + "B" * 300 + "C" * 200
    compressed, ratio = rle_compress(sample_data)
    print(compressed)
    print(ratio)