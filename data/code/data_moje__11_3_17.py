def safe_get_last(lst, default=None):
    if not lst:
        return default
    return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    empty_list = []
    print(safe_get_last(sample_list))
    print(safe_get_last(empty_list, "No elements"))