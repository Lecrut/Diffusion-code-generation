def get_last_item_pop(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    result = get_last_item_pop(test_list)
    print(result)
    print(test_list)
    empty_list = []
    result_empty = get_last_item_pop(empty_list)
    print(result_empty)
    print(empty_list)