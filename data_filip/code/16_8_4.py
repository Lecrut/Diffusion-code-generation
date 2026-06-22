def run_length_encode(data):
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
            result[current_element] = count
            current_element = element
            count = 1
    result[current_element] = count
    return result

if __name__ == '__main__':
    sample_tuple = (1, 1, 1, 2, 2, 3, 3, 3, 3)
    encoded = run_length_encode(sample_tuple)
    print(encoded)