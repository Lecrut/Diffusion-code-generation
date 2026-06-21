def join_lists(list1, list2):
    return [*list1, *list2]

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [40, 50, 60]
    result = join_lists(list_a, list_b)
    print(result)