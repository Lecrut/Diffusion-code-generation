def compress_floats_rle(data, tolerance=1e-9):
    if not data:
        return []
    result = []
    current_value = data[0]
    run_length = 1
    for i in range(1, len(data)):
        if abs(data[i] - current_value) <= tolerance:
            run_length += 1
        else:
            result.append((current_value, run_length))
            current_value = data[i]
            run_length = 1
    result.append((current_value, run_length))
    return result

def decompress_floats_rle(compressed):
    result = []
    for value, count in compressed:
        result.extend([value] * count)
    return result

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.5, 2.5, 3.1415926535, 3.1415926536, 4.0, 4.0, 5.5]
    compressed = compress_floats_rle(sample_data)
    print(compressed)
    decompressed = decompress_floats_rle(compressed)
    print(decompressed)