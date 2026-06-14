def find_average_of_set_elements(list_of_sets):
    union_set = set()
    for s in list_of_sets:
        union_set.update(s)
    if not union_set:
        return 0.0
    total_sum = sum(union_set)
    count = len(union_set)
    return total_sum / count
if __name__ == '__main__':
    list_of_sets_sample = [
        {1, 2, 3},
        {3, 4, 5},
        {5, 6, 7}
    ]
    average = find_average_of_set_elements(list_of_sets_sample)
    print(average)