def filter_and_intersect(list1, list2):
    def is_hashable(item):
        try:
            hash(item)
            return True
        except TypeError:
            return False

    filtered_list1 = [item for item in list1 if is_hashable(item)]
    filtered_list2 = [item for item in list2 if is_hashable(item)]
    set1 = set(filtered_list1)
    set2 = set(filtered_list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

if __name__ == '__main__':
    list_a = [1, 2, 2, 3, 4, 4, 5]
    list_b = [3, 4, 5, 'a', [], set()]
    common = filter_and_intersect(list_a, list_b)
    print(common)