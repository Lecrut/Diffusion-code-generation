def get_third_element(iterable):
    it = iter(iterable)
    try:
        next(it)
        next(it)
        return next(it)
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_third_element(sample_list))
    sample_tuple = (10, 20, 30)
    print(get_third_element(sample_tuple))
    sample_short = [1, 2]
    print(get_third_element(sample_short))
    sample_gen = (x for x in range(10))
    print(get_third_element(sample_gen))