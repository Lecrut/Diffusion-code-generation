def concat_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both arguments must be lists")
    return list1 + list2

if __name__ == '__main__':
    try:
        result = concat_lists([1, 2], [3, 4])
        print(result)
    except ValueError as e:
        print(e)