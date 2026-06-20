def compare_elements(list1, list2, index):
    return list1[index] <= list2[index]

if __name__ == '__main__':
    sample_list_a = [5, 3, 9]
    sample_list_b = [4, 6, 8]
    sample_index = 1
    result = compare_elements(sample_list_a, sample_list_b, sample_index)
    print(result)