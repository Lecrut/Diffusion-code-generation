def are_lists_equal(list1, list2):
    for elem1, elem2 in zip(list1, list2):
        if elem1 != elem2:
            yield False
            return
    yield True
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [1, 2, 4]
    result_ab = next(are_lists_equal(list_a, list_b))
    result_ac = next(are_lists_equal(list_a, list_c))
    print(result_ab)
    print(result_ac)