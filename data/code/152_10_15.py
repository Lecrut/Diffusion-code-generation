def intersect_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5, 5]
    sample_list_b = [4, 5, 6, 7, 8, 4]
    result = intersect_lists(sample_list_a, sample_list_b)
    print(result)