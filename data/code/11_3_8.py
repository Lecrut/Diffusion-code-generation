def safe_get_last_item(lst, default=None):
    if len(lst) == 0:
        return default
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    empty_list = []
    result1 = safe_get_last_item(sample_list, "No items")
    print(result1)
    result2 = safe_get_last_item(empty_list, "No items")
    print(result2)
    result3 = safe_get_last_item([42], 0)
    print(result3)