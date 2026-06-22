def safe_last_item(items, default=None):
    if len(items) == 0:
        return default
    return items[-1]

if __name__ == '__main__':
    data_list = [10, 20, 30, 40, 50]
    empty_list = []
    result_existing = safe_last_item(data_list)
    result_empty = safe_last_item(empty_list, default="No items")
    print(result_existing)
    print(result_empty)