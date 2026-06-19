def find_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.difference(set2))

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [30, 40, 50, 60, 70]
    result = find_difference(sample_list1, sample_list2)
    print(result)