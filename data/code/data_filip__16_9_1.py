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

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.000000001, 2.5, 2.5, 3.0, 3.0, 3.0, 3.0, 4.0]
    result = compress_floats(sample_data)
    print(result)