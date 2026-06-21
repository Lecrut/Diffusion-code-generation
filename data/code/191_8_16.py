def validate_lists(list1, list2):
    if not all(isinstance(item, (int, float)) for item in list1 + list2):
        raise ValueError("Both lists must contain only numbers.")

def concatenate_lists(list1, list2):
    validate_lists(list1, list2)
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)