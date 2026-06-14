def compute_average_of_sets(list_of_sets):
    if not list_of_sets:
        return 0
    total_sum = 0
    total_count = 0
    for s in list_of_sets:
        for item in s:
            total_sum += item
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
    average = compute_average_of_sets(sample_data)
    print(average)
    empty_data = []
    average_empty = compute_average_of_sets(empty_data)
    print(average_empty)
    single_set_data = [{10, 20}]
    average_single = compute_average_of_sets(single_set_data)
    print(average_single)