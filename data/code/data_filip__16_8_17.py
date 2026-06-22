def run_length_encode(data):
    if not data:
        return {}
    
    result = {}
    current_element = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_element:
            count += 1
        else:
            if current_element not in result:
                result[current_element] = count
            else:
                result[current_element] += count
            current_element = data[i]
            count = 1
    
    if current_element in result:
        result[current_element] += count
    else:
        result[current_element] = count
        
    return result

if __name__ == '__main__':
    sample_data = (1, 1, 2, 3, 3, 3, 2, 1)
    result = run_length_encode(sample_data)
    print(result)