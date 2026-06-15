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
    sets1 = [{1, 2}, {3, 4}, {2, 5}]
    print(find_average_of_set_elements(sets1))
    sets2 = [{10, 20}, {30, 40}, {50}]
    print(find_average_of_set_elements(sets2))
    sets3 = [set(), {1, 2, 3}, {4, 5}]
    print(find_average_of_set_elements(sets3))
    sets4 = [set(), set()]
    print(find_average_of_set_elements(sets4))