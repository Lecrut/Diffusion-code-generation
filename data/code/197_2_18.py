def validate_lists(list1, list2):
    if not isinstance(list1, list) or not all(isinstance(item, (int, str)) for item in list1):
        raise ValueError("First argument must be a list of strings or integers")
    if not isinstance(list2, list) or not all(isinstance(item, (int, str)) for item in list2):
        raise ValueError("Second argument must be a list of strings or integers")

def find_common_elements(list1, list2):
    validate_lists(list1, list2)
    return set(list1).intersection(list2)

if __name__ == '__main__':
    sample_list1 = ["Alice", "Bob", "Charlie", 4]
    sample_list2 = ["Bob", "David", 5, "Alice"]
    print(f"Common elements: {find_common_elements(sample_list1, sample_list2)}")