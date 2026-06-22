def get_last_item_safe(lst, default=None):
    if not lst:
        return default
    return lst[-1]

if __name__ == '__main__':
    print(get_last_item_safe([1, 2, 3]))
    print(get_last_item_safe([]))
    print(get_last_item_safe(['a', 'b', 'c'], 'default_value'))
    print(get_last_item_safe([], 'no_items'))