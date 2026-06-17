def find_minimum_generator(data):
    if not data:
        return
    current_min = data[0]
    yield current_min
    for item in data[1:]:
        if item < current_min:
            current_min = item
            yield current_min
if __name__ == '__main__':
    sample_sequence = [5, 2, 8, 1, 9, 3, 7]
    minimum_values = find_minimum_generator(sample_sequence)
    result = []
    for min_val in minimum_values:
        result.append(min_val)
    print(result)