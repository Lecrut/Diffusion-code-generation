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
    list4 = [5, 6, 7, 8]
    common1 = find_common_elements(list1, list2, list3)
    print(f"Common elements in {list1}, {list2}, and {list3}: {common1}")
    common2 = find_common_elements(list1, list4)
    print(f"Common elements in {list1} and {list4}: {common2}")
    common3 = find_common_elements([10, 20], [30, 40])
    print(f"Common elements in [10, 20] and [30, 40]: {common3}")
    common4 = find_common_elements([1, 2], [3, 4], [5, 6])
    print(f"Common elements in [1, 2], [3, 4], and [5, 6]: {common4}")
    common5 = find_common_elements([])
    print(f"Common elements in an empty set of lists: {common5}")