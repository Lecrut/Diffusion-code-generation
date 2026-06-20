def compare_elements(list1, list2, index):
    return list1[index] <= list2[index]

if __name__ == '__main__':
    sample_list1 = [3, 5, 2]
    sample_list2 = [4, 1, 6]
    sample_index = 1
    print(compare_elements(sample_list1, sample_list2, sample_index))