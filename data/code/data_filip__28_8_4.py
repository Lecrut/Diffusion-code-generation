def compress_rle(data):
    if not data:
        return []
    result = []
    count = 1
    current_val = data[0]
    for i in range(1, len(data)):
        val = data[i]
        if val == current_val:
            count += 1
        else:
            result.append((current_val, count))
            current_val = val
            count = 1
    result.append((current_val, count))
    return result

def decompress_rle(compressed):
    result = []
    for val, count in compressed:
        for _ in range(count):
            result.append(val)
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
    compressed = compress_rle(sample_data)
    print(compressed)
    decompressed = decompress_rle(compressed)
    print(decompressed)