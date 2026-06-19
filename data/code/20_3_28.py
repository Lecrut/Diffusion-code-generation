def are_lists_equal(list1, list2):
    for a, b in zip(list1, list2):
        if a != b:
            yield False
        else:
            yield True

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3, 5]
    
    result_generator = are_lists_equal(list1, list2)
    for result in result_generator:
        print(result)