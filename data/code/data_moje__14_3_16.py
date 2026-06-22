def get_third_element(iterable):
    iterator = iter(iterable)
    try:
        next(iterator)
        next(iterator)
        return next(iterator)
    except StopIteration:
        raise IndexError("Iterable has fewer than three elements")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c', 'd')
    print(get_third_element(sample_list))
    print(get_third_element(sample_tuple))