def average_of_set_union(list_of_sets):
    if not list_of_sets:
        return 0.0
    union_set = set()
    for s in list_of_sets:
        union_set.update(s)
    total_sum = sum(union_set)
    total_count = len(union_set)
    if total_count == 0:
        return 0.0
    else:
        return total_sum / total_count
if __name__ == '__main__':
    list_of_sets_sample = [
        {1, 2, 3},
        {3, 4, 5},
        {5, 6, 7}
    ]
    result = average_of_set_union(list_of_sets_sample)
    print(result)