def rle_compress(data):
    if not data:
        return "", 0.0
    compressed = []
    count = 1
    length = len(data)
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(str(count) + data[i - 1])
            count = 1
    compressed.append(str(count) + data[length - 1])
    compressed_str = "".join(compressed)
    ratio = len(data) / len(compressed_str) if compressed_str else 0.0
    return compressed_str, ratio

if __name__ == "__main__":
    sample_data = "A" * 500 + "B" * 300 + "C" * 200
    result_string, result_ratio = rle_compress(sample_data)
    print(result_string)
    print(result_ratio)