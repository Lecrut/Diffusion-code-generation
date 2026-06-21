def concatenate_string_lists(list1, list2):
    if not all(isinstance(item, str) for item in list1 + list2):
        raise ValueError("Both lists must contain only strings.")
    return list1 + list2

if __name__ == '__main__':
    sample_list_a = ["apple", "banana"]
    sample_list_b = ["cherry", "date"]
    try:
        result = concatenate_string_lists(sample_list_a, sample_list_b)
        print(result)
    except ValueError as e:
        print(e)