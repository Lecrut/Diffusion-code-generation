def get_third_element(iterable):
    iterator = iter(iterable)
    try:
        next(iterator)
        next(iterator)
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd')
    sample_generator = (x * 2 for x in range(10))
    
    print(get_third_element(sample_list))
    print(get_third_element(sample_tuple))
    print(get_third_element(sample_generator))