def validate_lists(list1, list2):
    if not all(isinstance(item, str) for item in list1 + list2):
        raise ValueError("Both lists must contain only strings")

def concatenate_string_lists(list1, list2):
    validate_lists(list1, list2)
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = ["apple", "banana"]
    sample_list2 = ["cherry", "date"]
    result = concatenate_string_lists(sample_list1, sample_list2)
    print(result)