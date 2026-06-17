def compare_lists(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    only_in_a = list(set_a - set_b)
    only_in_b = list(set_b - set_a)
    common = list(set_a.intersection(set_b))
    return {
        "only_in_list_a": only_in_a,
        "only_in_list_b": only_in_b,
        "common_elements": common
    }
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    result = compare_lists(list1, list2)
    print(result)