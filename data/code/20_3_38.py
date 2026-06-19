def are_lists_equal(list1, list2):
    for a, b in zip(list1, list2):
        if a != b:
            yield False
            return
    yield True
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    result1 = next(are_lists_equal(list1, list2))
    result2 = next(are_lists_equal(list1, list3))
    print(result1)
    print(result2)