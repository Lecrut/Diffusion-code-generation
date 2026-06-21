def find_first_difference_index(list1, list2):
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        if list1[i] != list2[i]:
            return i
    return -1

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 4, 4, 5]
    print(find_first_difference_index(sample_list1, sample_list2))