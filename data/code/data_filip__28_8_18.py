def compress_run_length(data):
    if not data:
        return []
    
    result = []
    current_value = data[0]
    count = 1
    
    for i in range(1, len(data)):
        value = data[i]
        if value == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = value
            count = 1
    
    result.append((current_value, count))
    
    return result

def decompress_run_length(encoded_data):
    if not encoded_data:
        return []
    
    result = []
    for value, count in encoded_data:
        result.extend([value] * count)
    
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
    compressed = compress_run_length(sample_data)
    print(compressed)
    decompressed = decompress_run_length(compressed)
    print(decompressed)