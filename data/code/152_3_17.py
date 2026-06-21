def validate_lists(list1, list2):
    if not all(isinstance(item, (int, str)) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers and strings")

def get_intersection(list1, list2):
    validate_lists(list1, list2)
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = get_intersection(list_a, list_b)
    print(result)