def are_lists_equal(list1, list2):
    for a, b in zip(list1, list2):
        yield a == b

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    list_c = [1, 2, 5, 4]

    result_ab = list(are_lists_equal(list_a, list_b))
    result_ac = list(are_lists_equal(list_a, list_c))

    print(result_ab)
    print(result_ac)