def run_length_encode(data):
    if not data:
        return {}
    result = {}
    count = 0
    current_element = data[0]
    for element in data:
        if element == current_element:
            count += 1
        else:
            result[current_element] = count
            current_element = element
            count = 1
    result[current_element] = count
    return result

if __name__ == '__main__':
    sample_data = ('a', 'a', 'b', 'b', 'b', 'c')
    encoded = run_length_encode(sample_data)
    print(encoded)