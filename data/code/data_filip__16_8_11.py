def run_length_encode(elements):
    if not elements:
        return {}
    result = {}
    current_element = elements[0]
    count = 1
    for i in range(1, len(elements)):
        if elements[i] == current_element:
            count += 1
        else:
            if current_element in result:
                result[current_element] += count
            else:
                result[current_element] = count
            current_element = elements[i]
            count = 1
    if current_element in result:
        result[current_element] += count
    else:
        result[current_element] = count
    return result

if __name__ == '__main__':
    sample_tuple = ('A', 'A', 'B', 'B', 'B', 'C', 'A', 'A')
    encoded_dict = run_length_encode(sample_tuple)
    print(encoded_dict)