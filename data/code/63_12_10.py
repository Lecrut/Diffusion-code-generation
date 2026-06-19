def get_first_item(iterable):
    return next(iter(iterable), None)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4]
    sample_tuple = (5, 6, 7, 8)
    empty_list = []
    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))
    print(get_first_item(empty_list))