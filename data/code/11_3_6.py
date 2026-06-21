def get_last_item(lst, default=None):
    if lst:
        return lst[-1]
    return default

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    empty_list = []
    print(get_last_item(sample_list))
    print(get_last_item(empty_list))
    print(get_last_item(empty_list, default="Empty"))
    print(get_last_item(sample_list, default="Empty"))