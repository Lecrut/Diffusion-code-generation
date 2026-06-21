def intersect_lists_ordered(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2]

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5, 5, 6]
    sample_list_b = [5, 4, 3, 7, 8, 9, 5]
    result = intersect_lists_ordered(sample_list_a, sample_list_b)
    print(result)