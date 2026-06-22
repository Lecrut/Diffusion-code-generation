def run_length_encode_tuple(data):
    if not data:
        return {}
    
    result = {}
    current_element = data[0]
    count = 1
    
    for i in range(1, len(data)):
        element = data[i]
        if element == current_element:
            count += 1
        else:
            result[(current_element, count)] = current_element
            current_element = element
            count = 1
    
    result[(current_element, count)] = current_element
    return result

def run_length_encode_to_count_map(data):
    if not data:
        return {}
    
    result = {}
    current_element = data[0]
    count = 1
    
    for i in range(1, len(data)):
        element = data[i]
        if element == current_element:
            count += 1
        else:
            if current_element in result:
                result[current_element] += count
            else:
                result[current_element] = count
            current_element = element
            count = 1
    
    if current_element in result:
        result[current_element] += count
    else:
        result[current_element] = count
    
    return result

if __name__ == '__main__':
    sample_data = ('a', 'a', 'b', 'b', 'b', 'c', 'a', 'a')
    print(run_length_encode_to_count_map(sample_data))