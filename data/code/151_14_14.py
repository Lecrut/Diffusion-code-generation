def concatenate_lists(list1: list, list2: list) -> list:
    if isinstance(list1, list) and isinstance(list2, list):
        return list1 + list2
    else:
        raise ValueError("Both inputs must be lists")

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [10, 11, 12]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)