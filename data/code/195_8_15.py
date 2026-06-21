def compare_lists(list1, list2):
    return [(i, (list1[i], list2[i])) for i in range(len(list1)) if list1[i] != list2[i]]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [1, 2, 5, 4]
    print(compare_lists(sample_list1, sample_list2))