def get_last_item(lst, default=None):
    if len(lst) > 0:
        return lst[-1]
    return default

if __name__ == '__main__':
    print(get_last_item([1, 2, 3]))
    print(get_last_item([]))
    print(get_last_item([], "empty"))