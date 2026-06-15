def compute_average_of_sets(list_of_sets):
    if not list_of_sets:
        return 0
    total_sum = 0
    total_count = 0
    for s in list_of_sets:
        total_sum += sum(s)
        total_count += len(s)
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    sample_data = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    result1 = compute_average_of_sets(sample_data)
    print(result1)
    empty_data = []
    result2 = compute_average_of_sets(empty_data)
    print(result2)
    single_set_data = [{10, 20}]
    result3 = compute_average_of_sets(single_set_data)
    print(result3)