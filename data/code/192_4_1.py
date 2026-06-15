def find_common_elements(list_a, list_b, list_c):
    set_a = set(list_a)
    set_b = set(list_b)
    set_c = set(list_c)
    common_elements = set_a.intersection(set_b).intersection(set_c)
    return list(common_elements)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]
    list_c = [4, 5, 8, 1, 9]
    result = find_common_elements(list_a, list_b, list_c)
    print(result)