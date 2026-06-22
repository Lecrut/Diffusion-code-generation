def find_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    difference_set = set1 - set2
    return list(difference_set)
if __name__ == '__main__':
    sample_list1 = [3, 6, 9, 12, 15]
    sample_list2 = [6, 12, 18, 24, 30]
    result = find_difference(sample_list1, sample_list2)
    print(result)