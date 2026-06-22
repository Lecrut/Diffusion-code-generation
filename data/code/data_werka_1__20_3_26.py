def are_lists_equal(list1, list2):
    for a, b in zip(list1, list2):
        if a != b:
            yield False
            return
    yield True
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 4, 3]
    generator_equal = are_lists_equal(list1, list2)
    print(next(generator_equal))
    generator_not_equal = are_lists_equal(list1, list3)
    print(next(generator_not_equal))