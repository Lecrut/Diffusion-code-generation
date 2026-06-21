def validate_lists(list1, list2):
    if not all(isinstance(item, int) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers")

def concatenate_lists(list1, list2):
    validate_lists(list1, list2)
    result = list1.copy()
    result.extend(list2)
    return result

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    final_result = concatenate_lists(sample_list_a, sample_list_b)
    print(final_result)