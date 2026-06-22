def compress_rle(data, tolerance=1e-9):
    if not data:
        return []
    
    compressed = []
    current_val = data[0]
    count = 1
    
    for i in range(1, len(data)):
        val = data[i]
        if abs(val - current_val) <= tolerance:
            count += 1
        else:
            compressed.append((current_val, count))
            current_val = val
            count = 1
    compressed.append((current_val, count))
    
    return compressed

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0000000001, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0]
    result = compress_rle(sample_data, tolerance=1e-8)
    print(result)