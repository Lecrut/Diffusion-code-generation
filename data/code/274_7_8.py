def validate_lists(list1, list2):
    if not all(isinstance(item, list) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists.")
    return list1, list2

def find_common_elements(list1, list2):
    common = set(list1).intersection(set(list2))
    return list(common)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    validated_lists = validate_lists(sample_list1, sample_list2)
    common_elements = find_common_elements(*validated_lists)
    print(common_elements)