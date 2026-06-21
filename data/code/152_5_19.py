def find_common_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    common_elements = set_a.intersection(set_b)
    sorted_common_elements = sorted(list(common_elements))
    return sorted_common_elements

if __name__ == '__main__':
    list_a_sample = [10, 20, 30, 40, 50, 60]
    list_b_sample = [30, 40, 50, 70, 80]
    result = find_common_elements(list_a_sample, list_b_sample)
    print(result)