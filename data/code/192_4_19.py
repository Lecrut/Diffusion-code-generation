def find_common_elements(list1, list2, tolerance=1e-09):
    return [x for x in list1 if any((abs(x - y) < tolerance for y in list2))]
if __name__ == '__main__':
    sample_list1 = [0.5, 1.5, 2.5]
    sample_list2 = [0.499, 1.501, 3.0]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(common_elements)