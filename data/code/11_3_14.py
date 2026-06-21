def safe_last_element(items, default=None):
    if not items:
        return default
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    empty_list = []
    print(safe_last_element(sample_list))
    print(safe_last_element(empty_list, "No items found"))