def run_length_encode(data):
    if not data:
        return {}
    
    result = {}
    current_element = data[0]
    current_count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_element:
            current_count += 1
        else:
            result[(current_element,)] = current_count
            current_element = data[i]
            current_count = 1
    
    result[(current_element,)] = current_count
    return result

if __name__ == '__main__':
    sample_tuple = ('a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a')
    encoded_result = run_length_encode(sample_tuple)
    print(encoded_result)