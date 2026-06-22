def find_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)

if __name__ == '__main__':
    sample_list1 = [5, 7, 9, 10, 12]
    sample_list2 = [8, 9, 10, 11, 13]
    result = find_difference(sample_list1, sample_list2)
    print(result)