def get_first_item(iterable):
    return next(iter(iterable), None)
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    sample_string = 'hello'
    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_string))
    print(get_first_item([]))
    print(get_first_item(()))
    print(get_first_item(''))