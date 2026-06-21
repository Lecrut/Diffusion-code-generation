def safe_last_item(lst, default=None):
    if not lst:
        return default
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    empty_list = []
    print(safe_last_item(sample_list))
    print(safe_last_item(empty_list))
    print(safe_last_item(empty_list, default="no items"))