def average_of_sets(list_of_sets):
    if not list_of_sets:
        return 0
    total_sum = 0
    total_count = 0
    for s in list_of_sets:
        for x in s:
            total_sum += x
            total_count += 1
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    data = [
        {1, 2},
        {3, 4, 5},
        {6}
    ]
    result = average_of_sets(data)
    print(result)
    empty_data = []
    result_empty = average_of_sets(empty_data)
    print(result_empty)
    single_element_data = [{10}]
    result_single = average_of_sets(single_element_data)
    print(result_single)