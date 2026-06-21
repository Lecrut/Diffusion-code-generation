def concatenate_lists(list1, list2):
    if not all(isinstance(item, list) and all(isinstance(elem, str) for elem in item) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists of strings")
    return list1 + list2

if __name__ == '__main__':
    try:
        sample_list_a = ["apple", "banana"]
        sample_list_b = ["cherry", "date"]
        result = concatenate_lists(sample_list_a, sample_list_b)
        print(result)
    except ValueError as e:
        print(e)