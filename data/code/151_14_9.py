def concatenate_lists(list_a: list, list_b: list) -> list:
    if isinstance(list_a, list) and isinstance(list_b, list):
        return list_a + list_b
    else:
        raise ValueError("Both inputs must be lists")

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)