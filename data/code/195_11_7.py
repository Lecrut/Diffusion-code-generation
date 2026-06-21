def intersect_lists(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50, 60]
    sample_list2 = [30, 40, 50, 70, 80]
    result = intersect_lists(sample_list1, sample_list2)
    print(result)