def run_length_encoding(t):
    if not t:
        return {}
    
    result = {}
    current_count = 0
    current_element = None
    
    for element in t:
        if current_element is None:
            current_element = element
            current_count = 1
        elif element == current_element:
            current_count += 1
        else:
            result[current_element] = current_count
            current_element = element
            current_count = 1
    
    if current_element is not None:
        result[current_element] = current_count
    
    return result

if __name__ == '__main__':
    sample_tuple = (1, 1, 1, 2, 3, 3, 2, 2, 2, 2)
    encoded = run_length_encoding(sample_tuple)
    print(encoded)