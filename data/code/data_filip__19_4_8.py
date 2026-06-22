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
            result.append([count, current_value])
            current_value = data[i]
            count = 1
            
    result.append([count, current_value])
    return result

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
    encoded = run_length_encode(sample_list)
    print(encoded)
    
    empty_list = []
    encoded_empty = run_length_encode(empty_list)
    print(encoded_empty)
    
    single_element = [42]
    encoded_single = run_length_encode(single_element)
    print(encoded_single)
    
    alternating = [1, 2, 1, 2, 1]
    encoded_alternating = run_length_encode(alternating)
    print(encoded_alternating)