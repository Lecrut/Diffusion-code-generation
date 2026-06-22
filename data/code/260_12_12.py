def compare_lists(list1, list2):
    return [item for item in list1 if item in list2] + [item for item in list2 if item not in list1]

if __name__ == '__main__':
    sample_list1 = [1.1, 2.2, 3.3, 4.4]
    sample_list2 = [3.3, 4.4, 5.5, 6.6]
    result = compare_lists(sample_list1, sample_list2)
    print(result)