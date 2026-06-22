def compress_floats_rle(data, tolerance=1e-9):
    if not data:
        return []
    
    result = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if abs(data[i] - current_value) <= tolerance:
            count += 1
        else:
            result.append((current_value, count))
            current_value = data[i]
            count = 1
    
    result.append((current_value, count))
    return result

def decompress_floats_rle(compressed_data):
    result = []
    for value, count in compressed_data:
        result.extend([value] * count)
    return result

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 4.0]
    compressed = compress_floats_rle(sample_data)
    print(compressed)
    decompressed = decompress_floats_rle(compressed)
    print(decompressed)