def get_last_item(lst, default=None):
    if lst:
        return lst[-1]
    return default

if __name__ == '__main__':
    data = [1, 2, 3]
    empty = []
    print(get_last_item(data))
    print(get_last_item(empty))
    print(get_last_item(empty, "default"))
    print(get_last_item(data, "default"))