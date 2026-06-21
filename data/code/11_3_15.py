def get_last_item_safe(lst, default=None):
    if not lst:
        return default
    return lst[-1]

if __name__ == '__main__':
    print(get_last_item_safe([1, 2, 3]))
    print(get_last_item_safe([], "empty"))
    print(get_last_item_safe(["apple", "banana"]))
    print(get_last_item_safe([], 0))