def safe_get_last(lst, default=None):
    if lst:
        return lst[-1]
    return default

if __name__ == '__main__':
    print(safe_get_last([1, 2, 3]))
    print(safe_get_last([], "empty"))