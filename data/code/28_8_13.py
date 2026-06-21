def compress_run_length(int_list):
    if not int_list:
        return []
    
    result = []
    current_value = int_list[0]
    count = 1
    
    for i in range(1, len(int_list)):
        if int_list[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = int_list[i]
            count = 1
    
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6, 6]
    compressed = compress_run_length(sample_data)
    print(compressed)
    
    empty_data = []
    compressed_empty = compress_run_length(empty_data)
    print(compressed_empty)
    
    single_element = [42]
    compressed_single = compress_run_length(single_element)
    print(compressed_single)
    
    alternating = [1, 2, 1, 2, 1, 2]
    compressed_alternating = compress_run_length(alternating)
    print(compressed_alternating)