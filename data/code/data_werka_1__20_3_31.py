def compare_lists(list1, list2):
    for item1, item2 in zip(list1, list2):
        if item1 != item2:
            yield False
            return
    yield True
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 4]
    list_c = [1, 2, 3, 5]
    for result in compare_lists(list_a, list_b):
        print(result)
    for result in compare_lists(list_a, list_c):
        print(result)