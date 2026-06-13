def find_common_elements(*lists):
    if not lists:
        return set()
    first_set = set(lists[0])
    for lst in lists[1:]:
        current_set = set(lst)
        first_set = first_set.intersection(current_set)
        if not first_set:
            return set()
    return first_set
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [4, 5, 8, 9, 10]
    list4 = [5, 6, 7, 11, 12]
    common1 = find_common_elements(list1, list2, list3, list4)
    print(f"Common elements: {common1}")
    list_a = ['apple', 'banana', 'cherry']
    list_b = ['banana', 'date', 'apple']
    list_c = ['apple', 'grape', 'banana']
    common2 = find_common_elements(list_a, list_b, list_c)
    print(f"Common elements: {common2}")
    list_x = [10, 20]
    list_y = [30, 40]
    common3 = find_common_elements(list_x, list_y)
    print(f"Common elements: {common3}")
    empty_lists = []
    common4 = find_common_elements(empty_lists, [1, 2], [])
    print(f"Common elements (with empty list): {common4}")