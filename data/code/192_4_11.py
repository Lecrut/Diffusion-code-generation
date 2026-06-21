def find_common_elements(list_a, list_b, tolerance=1e-9):
    if not all(isinstance(x, float) for x in list_a + list_b):
        raise ValueError("Both lists must contain only floats.")
    
    return [x for x in list_a if any(abs(x - y) < tolerance for y in list_b)]

if __name__ == '__main__':
    sample_list1 = [0.1 + 0.2, 0.3, 0.4]
    sample_list2 = [0.3000000001, 0.5, 0.6]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(common_elements)