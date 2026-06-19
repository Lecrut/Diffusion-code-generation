def find_unique_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_items = set1 - set2
    return list(unique_items)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result = find_unique_items(sample_list1, sample_list2)
    print(result)