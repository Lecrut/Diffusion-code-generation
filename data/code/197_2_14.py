def validate_lists(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples")
    return set(list1), set(list2)

def find_common_elements(list1, list2):
    validated_list1, validated_list2 = validate_lists(list1, list2)
    return validated_list1.intersection(validated_list2)

if __name__ == '__main__':
    sample_list1 = ["Alice", "Bob", "Charlie"]
    sample_list2 = ["Bob", "David", "Eve"]
    print(find_common_elements(sample_list1, sample_list2))