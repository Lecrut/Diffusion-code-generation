def get_first_item(iterable):
    return next(iter(iterable), None)
if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    sample_list = [4, 5, 6]
    sample_empty_list = []
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_list))
    print(get_first_item(sample_empty_list))