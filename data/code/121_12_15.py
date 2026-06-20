def compare_lists(a, b):
    if len(a) > len(b):
        return a
    elif len(b) > len(a):
        return b
    else:
        return None

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5]
    result = compare_lists(list1, list2)
    print(result)

    list3 = [1, 2, 3]
    list4 = [4, 5, 6, 7]
    result = compare_lists(list3, list4)
    print(result)

    list5 = [1, 2, 3]
    list6 = [1, 2, 3]
    result = compare_lists(list5, list6)
    print(result)