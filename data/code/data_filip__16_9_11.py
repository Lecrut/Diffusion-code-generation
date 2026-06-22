def compress_rle(data):
    if not data:
        return []
    
    result = []
    current_val = data[0]
    count = 1
    epsilon = 1e-9
    
    for i in range(1, len(data)):
        val = data[i]
        if abs(val - current_val) < epsilon:
            count += 1
        else:
            result.append((current_val, count))
            current_val = val
            count = 1
    result.append((current_val, count))
    return result

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.5, 2.5, 3.14159, 3.14159, 3.14159, 3.14159, 4.0]
    compressed = compress_rle(sample_data)
    print(compressed)