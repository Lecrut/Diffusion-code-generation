def intersect_lists(list1, list2):
    return set(list1) & set(list2)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50, 60]
    sample_list2 = [30, 40, 50, 70, 80, 90]
    result = intersect_lists(sample_list1, sample_list2)
    print(result)