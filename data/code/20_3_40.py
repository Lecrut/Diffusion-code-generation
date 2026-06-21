def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if item1 != item2:
            yield False
        else:
            yield True

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 4]
    result_generator = are_lists_equal(list1, list2)
    for result in result_generator:
        print(result)