def find_common_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    common_elements = set_a & set_b
    return list(common_elements)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50, 60]
    sample_list2 = [40, 50, 70, 80, 90, 10]
    result = find_common_elements(sample_list1, sample_list2)
    print(result)