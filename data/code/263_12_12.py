def intersect_lists(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples")
    
    return list(set(list1) & set(list2))

if __name__ == '__main__':
    print(intersect_lists([1, 2, 3, 4], [3, 4, 5, 6]))
    print(intersect_lists(['a', 'b', 'c'], ['c', 'd', 'e']))
    print(intersect_lists((1, 2), (2, 3)))