def find_first_difference_index(list1, list2):
    min_length = min(len(list1), len(list2))
    for index in range(min_length):
        if list1[index] != list2[index]:
            return index
    if len(list1) != len(list2):
        return min_length
    return -1

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 8, 4, 5]
    print(find_first_difference_index(sample_list1, sample_list2))