def merge_lists(list1, list2):
    return [*list1, *list2]

if __name__ == '__main__':
    LIST_A = [1, 2, 3]
    LIST_B = ['a', 'b', 'c']
    result = merge_lists(LIST_A, LIST_B)
    print(result)