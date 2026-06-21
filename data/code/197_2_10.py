def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return set(list1), set(list2)

def find_common_elements(list1, list2):
    return list(validate_lists(list1, list2)[0] & validate_lists(list1, list2)[1])

if __name__ == '__main__':
    sample_list1 = ["Alice", "Bob", "Charlie"]
    sample_list2 = ["Bob", "David", "Eve"]
    common_elements = find_common_elements(sample_list1, sample_list2)
    print(f"Common elements: {common_elements}")