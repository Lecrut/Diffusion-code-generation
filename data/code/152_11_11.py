def validate_lists(list1, list2):
    if not all(isinstance(item, int) for item in list1 + list2):
        raise ValueError("Both lists should contain only integers.")
    if len(set(list1)) != len(list1):
        raise ValueError("List 1 contains duplicates, which is not allowed.")
    if len(set(list2)) != len(list2):
        raise ValueError("List 2 contains duplicates, which is not allowed.")

def find_intersection_ordered(list1, list2):
    validate_lists(list1, list2)
    set2 = set(list2)
    return [item for item in list1 if item in set2]

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5]
    sample_list_b = [4, 5, 6, 7, 8]
    result = find_intersection_ordered(sample_list_a, sample_list_b)
    print(result)