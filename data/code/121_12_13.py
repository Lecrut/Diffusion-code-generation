def compare_lists(list1, list2):
    if len(list1) > len(list2):
        return list1
    elif len(list2) > len(list1):
        return list2
    else:
        return None

if __name__ == '__main__':
    print(compare_lists([1, 2, 3], [4, 5]))
    print(compare_lists(['a', 'b'], ['c', 'd', 'e']))
    print(compare_lists([], []))
    print(compare_lists([10], [10]))