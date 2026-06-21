def combine_lists(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both arguments must be lists")
    list_a.extend(list_b)

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combine_lists(list1, list2)
    print(list1)