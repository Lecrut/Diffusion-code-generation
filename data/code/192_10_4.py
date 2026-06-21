def find_common_elements(*lists):
    set_lists = [set(lst) for lst in lists]
    common_elements = set.intersection(*set_lists)
    return sorted(list(common_elements))

if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50, 50]
    list_b = [40, 50, 60, 70, 80, 40]
    list_c = [30, 40, 50, 90, 100, 30]
    result = find_common_elements(list_a, list_b, list_c)
    print(result)