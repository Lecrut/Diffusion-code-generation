def combine_lists(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists")
    list_a.extend(list_b)
    return list_a

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = combine_lists(list1, list2)
    print(result)