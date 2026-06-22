def get_last_item_or_none(data_list):
    if not data_list:
        return None
    return data_list.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item_or_none(sample_list)
    print(result)
    empty_list = []
    result_empty = get_last_item_or_none(empty_list)
    print(result_empty)
    sample_list_2 = ["a", "b", "c"]
    result_2 = get_last_item_or_none(sample_list_2)
    print(result_2)
    sample_list_3 = []
    result_3 = get_last_item_or_none(sample_list_3)
    print(result_3)