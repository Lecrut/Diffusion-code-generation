def is_subset(list1, list2):
    return set(list1).issubset(set(list2))
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [4, 3, 2, 1, 5, 6]
    print(is_subset(sample_list1, sample_list2))