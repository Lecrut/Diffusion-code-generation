def run_length_encoding_sequence(data):
    if not data:
        return {}
    result = {}
    current_element = data[0]
    count = 1
    for element in data[1:]:
        if element == current_element:
            count += 1
        else:
            result[current_element] = count
            current_element = element
            count = 1
    result[current_element] = count
    return result

if __name__ == '__main__':
    sample_tuple = (1, 1, 1, 2, 3, 3, 2, 2)
    encoded = run_length_encoding_sequence(sample_tuple)
    print(encoded)