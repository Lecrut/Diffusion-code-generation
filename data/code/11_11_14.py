def get_last_item_pop(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item_pop(sample_list)
    print(result)

    empty_list = []
    result_empty = get_last_item_pop(empty_list)
    print(result_empty)

    single_item_list = [42]
    result_single = get_last_item_pop(single_item_list)
    print(result_single)