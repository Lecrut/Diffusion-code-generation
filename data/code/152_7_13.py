def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5, 6]
    sample_list2 = [4, 5, 6, 7, 8, 9, 9]
    print(find_common_elements(sample_list1, sample_list2))