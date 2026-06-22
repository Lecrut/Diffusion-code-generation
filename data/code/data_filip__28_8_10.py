def compress_rle(data):
    if not data:
        return []
    
    if len(data) == 1:
        return [(data[0], 1)]
    
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

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 1]
    compressed = compress_rle(sample_data)
    print(compressed)