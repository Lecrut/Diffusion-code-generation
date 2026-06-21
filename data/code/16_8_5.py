def run_length_encode(data):
    if not data:
        return {}
    counts = {}
    current_element = data[0]
    current_count = 1
    for i in range(1, len(data)):
        if data[i] == current_element:
            current_count += 1
        else:
            counts[current_element] = current_count
            current_element = data[i]
            current_count = 1
    counts[current_element] = current_count
    return counts

if __name__ == '__main__':
    sample_data = ('a', 'a', 'b', 'c', 'c', 'c', 'd', 'd')
    result = run_length_encode(sample_data)
    print(result)