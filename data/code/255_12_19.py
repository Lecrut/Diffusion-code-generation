def intersect_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 8, 15]
    sample_list_2 = [-5, -1, -10, -3, 10]
    result = intersect_lists(sample_list_1, sample_list_2)
    print(result)