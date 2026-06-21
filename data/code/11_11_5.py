def get_last_item_pop(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_item_pop(sample_list))

    empty_list = []
    print(get_last_item_pop(empty_list))

    single_item_list = [42]
    print(get_last_item_pop(single_item_list))