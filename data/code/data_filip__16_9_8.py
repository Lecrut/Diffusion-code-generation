def compress_rle(data):
    if not data:
        return []
    if len(data) == 1:
        return [(data[0], 1)]
    
    compressed = []
    current_val = data[0]
    count = 1
    
    for i in range(1, len(data)):
        current = data[i]
        if current == current_val:
            count += 1
        else:
            compressed.append((current_val, count))
            current_val = current
            count = 1
    compressed.append((current_val, count))
    return compressed

def decompress_rle(compressed_data):
    result = []
    for val, count in compressed_data:
        result.extend([val] * count)
    return result

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 2.5, 2.5, 2.5, 3.1, 3.1, 1.0, 1.0, 1.0, 2.5]
    compressed = compress_rle(sample_data)
    print(compressed)
    decompressed = decompress_rle(compressed)
    print(decompressed)