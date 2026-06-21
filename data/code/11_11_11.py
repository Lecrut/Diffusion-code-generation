def get_last_item_pop(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item_pop(sample_list)
    print(result)
    empty_list = []
    result_empty = get_last_item_pop(empty_list)
    print(result_empty)