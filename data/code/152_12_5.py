def find_unique_commons(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40]
    sample_list_b = [30, 40, 50, 60]
    result = find_unique_commons(sample_list_a, sample_list_b)
    print(result)