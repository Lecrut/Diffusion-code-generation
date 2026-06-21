def validate_lists(list_a, list_b):
    if not all(isinstance(item, (int, float)) for item in list_a + list_b):
        raise ValueError("Both lists must contain only numbers.")
    return True

def find_shared_elements(list_a, list_b):
    validate_lists(list_a, list_b)
    set_a = set(list_a)
    set_b = set(list_b)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(find_shared_elements(sample_list1, sample_list2))