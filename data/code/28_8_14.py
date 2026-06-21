def compress_integers(data):
    if not data:
        return []
    if len(data) == 1:
        return [(data[0], 1)]
    
    result = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = data[i]
            count = 1
    
    result.append((current_value, count))
    return result

def decompress_integers(rle_data):
    if not rle_data:
        return []
    
    result = []
    for value, count in rle_data:
        for _ in range(count):
            result.append(value)
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]
    compressed = compress_integers(sample_data)
    print(compressed)
    decompressed = decompress_integers(compressed)
    print(decompressed)