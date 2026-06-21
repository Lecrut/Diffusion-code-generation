def third_element(iterable):
    iterator = iter(iterable)
    next(iterator)
    next(iterator)
    return next(iterator)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = third_element(sample_list)
    print(result)