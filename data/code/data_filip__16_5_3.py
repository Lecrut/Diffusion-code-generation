def run_length_encode(sequence):
    if not sequence:
        return []
    
    encoded = []
    current_value = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_value:
            count += 1
        else:
            encoded.append([current_value, count])
            current_value = sequence[i]
            count = 1
    
    encoded.append([current_value, count])
    return encoded

if __name__ == '__main__':
    sample_input = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]
    result = run_length_encode(sample_input)
    print(result)
    
    empty_input = []
    result_empty = run_length_encode(empty_input)
    print(result_empty)
    
    single_element = [42]
    result_single = run_length_encode(single_element)
    print(result_single)
    
    all_same = [7, 7, 7, 7]
    result_same = run_length_encode(all_same)
    print(result_same)
    
    alternating = [1, 2, 1, 2, 1]
    result_alternating = run_length_encode(alternating)
    print(result_alternating)