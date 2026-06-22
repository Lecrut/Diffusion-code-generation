def run_length_encode(data):
    if not data:
        return []
    
    result = []
    current_count = 1
    current_value = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_value:
            current_count += 1
        else:
            result.append((current_value, current_count))
            current_value = data[i]
            current_count = 1
    
    result.append((current_value, current_count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 1]
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)