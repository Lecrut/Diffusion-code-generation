def find_unique_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_items = set1.difference(set2)
    return list(unique_items)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [30, 40, 50, 60, 70]
    result = find_unique_items(sample_list1, sample_list2)
    print(result)