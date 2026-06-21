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
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5]
    encoded = run_length_encode(sample_data)
    print(encoded)
    
    empty_data = []
    encoded_empty = run_length_encode(empty_data)
    print(encoded_empty)
    
    single_element = [42]
    encoded_single = run_length_encode(single_element)
    print(encoded_single)
    
    no_runs = [1, 2, 3, 4, 5]
    encoded_no_runs = run_length_encode(no_runs)
    print(encoded_no_runs)
    
    all_same = [7, 7, 7, 7, 7]
    encoded_all_same = run_length_encode(all_same)
    print(encoded_all_same)