def safe_last(items, default=None):
    if len(items) == 0:
        return default
    return items[-1]

if __name__ == '__main__':
    data_list = [10, 20, 30, 40, 50]
    empty_list = []
    print(safe_last(data_list))
    print(safe_last(empty_list, "No elements found"))