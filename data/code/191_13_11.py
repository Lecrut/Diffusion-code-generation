def merge_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both arguments must be lists")
    return list1 + list2

if __name__ == '__main__':
    try:
        list_a = [1, 2, 3]
        list_b = [4, 5, 6]
        combined = merge_lists(list_a, list_b)
        print(combined)
    except ValueError as e:
        print(e)