def compare_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists")
    return max((list1, list2), key=sum)

if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [5, 15, 25, 35]
    result = compare_lists(list_a, list_b)
    print(result)