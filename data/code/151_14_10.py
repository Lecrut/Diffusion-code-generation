def concatenate_lists(list1: list, list2: list) -> list:
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists")
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [40, 50, 60]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)