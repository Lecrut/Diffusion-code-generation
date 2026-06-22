def run_length_encode(data):
    if not data:
        return []
    
    encoded = []
    current_count = 1
    current_value = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_value:
            current_count += 1
        else:
            encoded.append([current_count, current_value])
            current_value = data[i]
            current_count = 1
    encoded.append([current_count, current_value])
    
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 1]
    result = run_length_encode(sample_data)
    print(result)
    
    empty_data = []
    empty_result = run_length_encode(empty_data)
    print(empty_result)