def merge_lists(list_a, list_b):
    return [*list_a, *list_b]

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = merge_lists(list_a, list_b)
    print(result)