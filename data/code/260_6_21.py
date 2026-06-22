def compare_float_lists(list1, list2):
    equal_indices = []
    for idx, (val1, val2) in enumerate(zip(list1, list2)):
        if abs(val1 - val2) < 1e-09:
            equal_indices.append(idx)
    return equal_indices

if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.0, 4.5]
    sample_list2 = [1.0, 2.6, 3.0, 4.499999999]
    print(compare_float_lists(sample_list1, sample_list2))