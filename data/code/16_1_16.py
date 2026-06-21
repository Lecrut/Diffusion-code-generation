def run_length_encode(data):
    if not data:
        return []
    
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

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6]
    compressed = run_length_encode(sample_list)
    print(compressed)
    
    sample_list_single = [1, 2, 3, 4, 5]
    compressed_single = run_length_encode(sample_list_single)
    print(compressed_single)
    
    sample_list_empty = []
    compressed_empty = run_length_encode(sample_list_empty)
    print(compressed_empty)
    
    sample_list_mixed = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 2, 2, 3, 3, 3, 4]
    compressed_mixed = run_length_encode(sample_list_mixed)
    print(compressed_mixed)