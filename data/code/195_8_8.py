def compare_lists(list1, list2):
    return [(x, y) for x, y in zip(list1, list2) if x != y]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [1, 2, 5, 4]
    print(compare_lists(sample_list1, sample_list2))