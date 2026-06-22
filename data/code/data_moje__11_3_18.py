def safe_get_last(lst, default=None):
    if not lst:
        return default
    return lst[-1]

if __name__ == '__main__':
    print(safe_get_last([1, 2, 3]))
    print(safe_get_last([]))
    print(safe_get_last(['a', 'b', 'c'], default='empty'))
    print(safe_get_last([], default='no items'))