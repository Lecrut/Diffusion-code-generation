def get_last_item_or_none(items):
    if not items:
        return None
    return items.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item_or_none(sample_list)
    print(result)
    print(sample_list)
    empty_list = []
    result_empty = get_last_item_or_none(empty_list)
    print(result_empty)