def validate_input(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Inputs must be lists or tuples")

def find_common_elements(list1, list2):
    set2 = set(list2)
    return [element for element in list1 if element in set2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    validate_input(sample_list1, sample_list2)
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(common_elements)