def concatenate_lists(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists")
    return list_a + list_b

if __name__ == '__main__':
    list_a_sample = [1, 2, 3]
    list_b_sample = [4, 5, 6]
    result = concatenate_lists(list_a_sample, list_b_sample)
    print(result)