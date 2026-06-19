def are_lists_equal(list1, list2):
    for item1, item2 in zip(list1, list2):
        if item1 != item2:
            yield False
        else:
            yield True

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [1, 2, 4]
    
    result_generator = are_lists_equal(list_a, list_b)
    results = list(result_generator)
    print(results)