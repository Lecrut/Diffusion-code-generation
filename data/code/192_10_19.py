def find_common_elements(*lists):
    set_args = map(set, lists)
    common_elements = set.intersection(*set_args)
    return sorted(common_elements)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    list_c = [4, 9, 10, 11, 5]
    result = find_common_elements(list_a, list_b, list_c)
    print(result)