def concatenate_lists(list_a: list, list_b: list) -> list:
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists")
    return list_a + list_b

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [40, 50, 60]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)