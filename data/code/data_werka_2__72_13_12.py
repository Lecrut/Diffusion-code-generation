def compare_elements_at_indices(list_one, list_two, target_indices):
    max_len = len(list_one) if len(list_one) > len(list_two) else len(list_two)
    comparisons = []
    for current_index in target_indices:
        is_valid_index = isinstance(current_index, int) and 0 <= current_index < max_len
        if not is_valid_index:
            comparisons.append(False)
        else:
            value_first = list_one[current_index] if current_index < len(list_one) else None
            value_second = list_two[current_index] if current_index < len(list_two) else None
            comparisons.append(value_first == value_second)
    return comparisons

if __name__ == '__main__':
    data_a = [100, 200, 300, 400]
    data_b = [100, 250, 300, 450]
    request_indices = [0, 2, 3, 5, -1]
    output_results = compare_elements_at_indices(data_a, data_b, request_indices)
    print(output_results)