def get_last_item_or_none(data_list):
    if not data_list:
        return None
    return data_list.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_last_item_or_none(sample_list)
    print(result)
    empty_list = []
    result_empty = get_last_item_or_none(empty_list)
    print(result_empty)