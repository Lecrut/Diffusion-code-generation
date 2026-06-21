def is_subset(list1, list2):
    return set(list1) <= set(list2)
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [3, 2, 1, 4, 5]
    print(is_subset(sample_list1, sample_list2))