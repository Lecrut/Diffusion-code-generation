def compare_lists(list1, list2):
    return [(x, y) for x, y in zip(list1, list2) if x != y]
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 5, 4]
    print(compare_lists(list_a, list_b))
    list_c = ['a', 'b', 'c']
    list_d = ['a', 'd', 'c']
    print(compare_lists(list_c, list_d))