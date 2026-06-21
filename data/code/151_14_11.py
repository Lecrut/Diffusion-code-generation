def concatenate_lists(list1, list2):
    if isinstance(list1, list) and isinstance(list2, list):
        return list1 + list2
    else:
        raise ValueError("Both inputs must be lists")

if __name__ == '__main__':
    result = concatenate_lists([1, 2, 3], [4, 5, 6])
    print(result)