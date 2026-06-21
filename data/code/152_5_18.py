def find_common_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    common_elements = set_a.intersection(set_b)
    sorted_common_elements = sorted(list(common_elements))
    return sorted_common_elements

if __name__ == '__main__':
    LIST_A_SAMPLE = [1, 5, 2, 8, 3, 5, 9]
    LIST_B_SAMPLE = [8, 3, 1, 9, 4, 5]
    result = find_common_elements(LIST_A_SAMPLE, LIST_B_SAMPLE)
    print(result)