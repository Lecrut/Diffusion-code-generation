def intersect_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9, 11]
    sample_list2 = [4, 5, 6, 7, 8]
    result = intersect_lists(sample_list1, sample_list2)
    print(result)