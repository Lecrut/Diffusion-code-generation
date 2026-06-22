def get_last_item(safe_list, default_value=None):
    if not safe_list:
        return default_value
    return safe_list[-1]

if __name__ == '__main__':
    print(get_last_item([1, 2, 3]))
    print(get_last_item([]))
    print(get_last_item([42], default_value="fallback"))
    print(get_last_item([], default_value="no items"))
    print(get_last_item([10, 20, 30], default_value=999))