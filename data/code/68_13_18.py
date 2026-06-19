def find_unique_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_items = set1.symmetric_difference(set2) - set2
    return list(unique_items)

if __name__ == '__main__':
    SAMPLE_LIST_1 = [10, 20, 30, 40, 50]
    SAMPLE_LIST_2 = [30, 40, 60, 70, 80]
    result = find_unique_items(SAMPLE_LIST_1, SAMPLE_LIST_2)
    print(result)