def get_last_item_or_none(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    result_1 = get_last_item_or_none(sample_list_1)
    print(result_1)
    print(sample_list_1)
    sample_list_2 = []
    result_2 = get_last_item_or_none(sample_list_2)
    print(result_2)