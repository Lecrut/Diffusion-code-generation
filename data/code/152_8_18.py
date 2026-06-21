def validate_lists(list1, list2):
    if not all(isinstance(item, (int, float)) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers or floats.")
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists.")

def find_intersection(list1, list2):
    validate_lists(list1, list2)
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result = find_intersection(sample_list1, sample_list2)
    print(result)