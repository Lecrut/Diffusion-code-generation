def intersect_lists(list1, list2):
    return [item for item in list1 if item in list2 and isinstance(item, hashable)]

if __name__ == '__main__':
    list_a = [1, 2, 3, (4,), {5}]
    list_b = [2, (4,), {5}, '6']
    common_elements = intersect_lists(list_a, list_b)
    print(common_elements)