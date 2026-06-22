def compress_rle(data):
    if not data:
        return []
    compressed = []
    current_value = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = data[i]
            count = 1
    compressed.append((current_value, count))
    return compressed

def decompress_rle(compressed_data):
    result = []
    for value, count in compressed_data:
        result.extend([value] * count)
    return result

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.5, 2.5, 3.14, 3.14, 3.14, 3.14, 0.0, 0.0]
    encoded = compress_rle(sample_data)
    decoded = decompress_rle(encoded)
    print(encoded)
    print(decoded)