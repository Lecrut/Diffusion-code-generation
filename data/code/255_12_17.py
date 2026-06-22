def intersect_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 8, 15, 5]
    sample_list2 = [20, 15, 30, 45]
    print(intersect_lists(sample_list1, sample_list2))