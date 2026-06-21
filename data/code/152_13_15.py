def validate_inputs(list1, list2):
    if not all(isinstance(item, (int, str)) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers or strings.")
    if len(list1) == 0 or len(list2) == 0:
        return frozenset(), frozenset()
    return frozenset(list1), frozenset(list2)

def get_intersection(list1, list2):
    set1, set2 = validate_inputs(list1, list2)
    return list(set1 & set2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = get_intersection(list_a, list_b)
    print(f"Intersection of {list_a} and {list_b}: {result1}")