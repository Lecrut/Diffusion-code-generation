def find_common_elements(*lists):
    if not lists:
        return set()
    first_set = set(lists[0])
    for lst in lists[1:]:
        current_set = set(lst)
        first_set = first_set.intersection(current_set)
        if not first_set:
            return []
    return list(first_set)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [4, 5, 8, 9, 10]
    list4 = [5, 6, 7, 11, 12]
    common1 = find_common_elements(list1, list2, list3)
    print(f"Common to {list1}, {list2}, {list3}: {common1}")
    common2 = find_common_elements(list1, list4)
    print(f"Common to {list1}, {list4}: {common2}")
    common3 = find_common_elements(list1)
    print(f"Common to {list1}: {common3}")
    common_empty = find_common_elements()
    print(f"Common to no lists: {common_empty}")
    list_a = ['a', 'b', 'c']
    list_b = ['c', 'd', 'e']
    list_c = ['c', 'f', 'g']
    common_letters = find_common_elements(list_a, list_b, list_c)
    print(f"Common to {list_a}, {list_b}, {list_c}: {common_letters}")