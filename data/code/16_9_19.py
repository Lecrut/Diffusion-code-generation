def compress_floats(data, tolerance=1e-9):
    if not data:
        return []

    compressed = []
    current_value = data[0]
    count = 1

    for i in range(1, len(data)):
        if abs(data[i] - current_value) <= tolerance:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = data[i]
            count = 1

    compressed.append((current_value, count))
    return compressed

def decompress_floats(compressed):
    data = []
    for value, count in compressed:
        data.extend([value] * count)
    return data

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 1.0, 1.0, 4.5, 4.5, 4.5, 4.5, 4.5]
    compressed = compress_floats(sample_data)
    print(compressed)
    decompressed = decompress_floats(compressed)
    print(decompressed)
    print(decompressed == sample_data)