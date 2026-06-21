def merge_lists(list_a, list_b):
    return [*list_a, *list_b]

if __name__ == '__main__':
    list_c = [10, 20, 30]
    list_d = [40, 50, 60]
    result = merge_lists(list_c, list_d)
    print(result)