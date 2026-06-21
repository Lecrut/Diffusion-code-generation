def compare_float_lists(list1, list2, tolerance=1e-9):
    return [x for x in list1 if any(abs(x - y) < tolerance for y in list2)]

if __name__ == '__main__':
    sample_list1 = [0.1 + 0.2, 0.3, 0.4]
    sample_list2 = [0.300000001, 0.5, 0.6]
    tolerance = 1e-9
    common_elements = compare_float_lists(sample_list1, sample_list2, tolerance)
    print(common_elements)