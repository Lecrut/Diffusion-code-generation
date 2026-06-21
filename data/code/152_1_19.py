def validate_lists(list_a, list_b):
    if not all(isinstance(item, (int, str)) for item in list_a + list_b):
        raise ValueError("Both lists should contain only integers or strings.")
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise TypeError("Both inputs must be lists.")

def find_common_elements_ordered(list1, list2):
    validate_lists(list1, list2)
    seen = set()
    common = []
    for item in list1:
        if item in list2 and item not in seen:
            common.append(item)
            seen.add(item)
    return common

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 6]
    sample_list2 = [4, 5, 6, 7, 8, 9]
    print(find_common_elements_ordered(sample_list1, sample_list2))