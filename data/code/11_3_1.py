def get_last_item(lst, default=None):
    if not lst:
        return default
    return lst[-1]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = []
    result_1 = get_last_item(sample_list_1)
    result_2 = get_last_item(sample_list_2, default="No items")
    print(result_1)
    print(result_2)