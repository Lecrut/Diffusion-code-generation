def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1 & set2
    return list(common_elements)

if __name__ == '__main__':
    sample_list_x = [10, 20, 30, 40, 50]
    sample_list_y = [40, 50, 60, 70, 80]
    common = find_common_elements(sample_list_x, sample_list_y)
    print(common)