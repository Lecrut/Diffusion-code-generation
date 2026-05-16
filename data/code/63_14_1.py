def get_first_item(iterable):
    return iterable[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))