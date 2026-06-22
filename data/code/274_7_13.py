def find_common_elements(list1, list2):
    common = set(list1).intersection(set(list2))
    return list(common)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(find_common_elements(sample_list1, sample_list2))