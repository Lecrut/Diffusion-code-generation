def is_subset(list1, list2):
    return all((item in list2 for item in list1))
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [1, 2, 3, 4, 5]
    print(is_subset(sample_list1, sample_list2))