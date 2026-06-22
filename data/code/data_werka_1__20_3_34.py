def are_lists_equal(list1, list2):
    for a, b in zip(list1, list2):
        if a != b:
            yield False
            return
    yield True
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [1, 2, 4]
    generator_ab = are_lists_equal(list_a, list_b)
    print(next(generator_ab))
    generator_ac = are_lists_equal(list_a, list_c)
    print(next(generator_ac))