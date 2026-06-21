def compress_floats(data, tolerance=1e-9):
    if not data:
        return []
    
    result = []
    current_value = data[0]
    run_length = 1
    
    for i in range(1, len(data)):
        if abs(data[i] - current_value) < tolerance:
            run_length += 1
        else:
            result.append((current_value, run_length))
            current_value = data[i]
            run_length = 1
    
    result.append((current_value, run_length))
    return result

if __name__ == '__main__':
    sample_data = [1.1, 1.1, 1.100000001, 2.2, 2.2, 3.3, 3.3, 3.3, 3.3]
    compressed = compress_floats(sample_data)
    print(compressed)
    
    empty_data = []
    print(compress_floats(empty_data))
    
    single_element = [42.0]
    print(compress_floats(single_element))
    
    all_different = [1.0, 2.0, 3.0, 4.0]
    print(compress_floats(all_different))