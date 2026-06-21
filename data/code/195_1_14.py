def find_first_mismatch(list1, list2):
    min_length = min(len(list1), len(list2))
    for index in range(min_length):
        if list1[index] != list2[index]:
            return index
    return -1
if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4]
    sample_list_b = [1, 2, 3, 4]
    sample_list_c = [1, 9, 3, 4]
    print(find_first_mismatch(sample_list_a, sample_list_b))
    print(find_first_mismatch(sample_list_a, sample_list_c))