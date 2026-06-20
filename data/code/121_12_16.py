def compare_lists(list1, list2):
    if len(list1) > len(list2):
        return list1
    elif len(list2) > len(list1):
        return list2
    else:
        return None

if __name__ == '__main__':
    result = compare_lists([1, 2, 3], [4, 5])
    print(result)