def safe_get_last(lst, default=None):
    if lst:
        return lst[-1]
    return default

if __name__ == '__main__':
    result1 = safe_get_last([1, 2, 3])
    print(result1)
    result2 = safe_get_last([], default="empty")
    print(result2)
    result3 = safe_get_last([])
    print(result3)