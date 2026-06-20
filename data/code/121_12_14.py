def compare_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    return list1 if len(list1) > len(list2) else list2 if len(list2) > len(list1) else None

if __name__ == '__main__':
    print(compare_lists([1, 2, 3], [4, 5]))
    print(compare_lists(['a', 'b'], ['c', 'd', 'e']))
    print(compare_lists([], []))
    try:
        print(compare_lists('not a list', [1, 2]))
    except ValueError as e:
        print(e)