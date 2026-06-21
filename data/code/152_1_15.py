def validate_lists(list_a, list_b):
    if not all(isinstance(item, (int, str)) for item in list_a + list_b):
        raise ValueError("Both lists must contain only integers or strings.")
    return list_a, list_b

def find_common_elements(list1, list2):
    common = []
    seen = set()
    for item in list1:
        if item in list2 and item not in seen:
            common.append(item)
            seen.add(item)
    return common

if __name__ == '__main__':
    list_a_sample = [1, 2, 3, 4, 5, 6]
    list_b_sample = [4, 5, 6, 7, 8, 9]
    validated_lists = validate_lists(list_a_sample, list_b_sample)
    result = find_common_elements(*validated_lists)
    print(result)