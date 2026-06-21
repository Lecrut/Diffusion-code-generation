def run_length_encode(elements):
    if not elements:
        return {}
    
    counts = {}
    current_element = elements[0]
    current_count = 1
    
    for i in range(1, len(elements)):
        if elements[i] == current_element:
            current_count += 1
        else:
            if current_element in counts:
                counts[current_element] += current_count
            else:
                counts[current_element] = current_count
            current_element = elements[i]
            current_count = 1
    
    if current_element in counts:
        counts[current_element] += current_count
    else:
        counts[current_element] = current_count
    
    return counts

if __name__ == '__main__':
    sample_data = ('a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a')
    result = run_length_encode(sample_data)
    print(result)