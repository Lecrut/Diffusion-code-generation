def compare_lists(list1, list2):
    return [(index, value1, value2) for index, (value1, value2) in enumerate(zip(list1, list2)) if value1 != value2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 3, 6, 5]
    print(compare_lists(sample_list1, sample_list2))