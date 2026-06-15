def compute_average_of_sets(list_of_sets):
    if not list_of_sets:
        return 0
    total_sum = 0
    total_count = 0
    for s in list_of_sets:
        for num in s:
            total_sum += num
            total_count += 1
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    sample_data = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    result = compute_average_of_sets(sample_data)
    print(result)
    empty_data = []
    result_empty = compute_average_of_sets(empty_data)
    print(result_empty)
    single_set_data = [{10, 20}]
    result_single = compute_average_of_sets(single_set_data)
    print(result_single)