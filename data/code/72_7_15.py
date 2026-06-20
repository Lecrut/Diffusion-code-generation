def is_first_less_or_equal(list1, list2, index):
    return list1[index] <= list2[index]

if __name__ == '__main__':
    sample_list1 = [3, 5, 7]
    sample_list2 = [4, 6, 8]
    sample_index = 1
    print(is_first_less_or_equal(sample_list1, sample_list2, sample_index))