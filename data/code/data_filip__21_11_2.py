def run_length_encode(input_list):
    if not input_list:
        return []
    
    encoded = []
    current_value = input_list[0]
    current_count = 1
    
    for i in range(1, len(input_list)):
        value = input_list[i]
        if value == current_value:
            current_count += 1
        else:
            encoded.append((current_value, current_count))
            current_value = value
            current_count = 1
            
    encoded.append((current_value, current_count))
    
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 4]
    result = run_length_encode(sample_data)
    print(result)