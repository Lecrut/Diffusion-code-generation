def find_adjacent_mismatches(sequence):
    indices_and_values = []
    limit = len(sequence)
    if limit < 2:
        return indices_and_values
    for current_index in range(limit - 1):
        first_element = sequence[current_index]
        second_element = sequence[current_index + 1]
        if first_element != second_element:
            indices_and_values.append((current_index, first_element, second_element))
    return indices_and_values

if __name__ == '__main__':
    test_values = [10, 10, 10, 20, 20, 30, 30, 30, 30, 40, 40, 50]
    mismatch_data = find_adjacent_mismatches(test_values)
    print(mismatch_data)