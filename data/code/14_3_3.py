def third_element(iterable):
    iterator = iter(iterable)
    next(iterator, None)
    next(iterator, None)
    return next(iterator, None)

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    result = third_element(sample_iterable)
    print(result)

    sample_string = "hello"
    result_string = third_element(sample_string)
    print(result_string)

    sample_generator = (x for x in range(10))
    result_gen = third_element(sample_generator)
    print(result_gen)

    sample_short = [1, 2]
    result_short = third_element(sample_short)
    print(result_short)