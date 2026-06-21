def get_third_element(sequence):
    iterator = iter(sequence)
    next(iterator, None)
    next(iterator, None)
    return next(iterator, None)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30, 40)
    sample_string = "hello"
    sample_short = [1]

    print(get_third_element(sample_list))
    print(get_third_element(sample_tuple))
    print(get_third_element(sample_string))
    print(get_third_element(sample_short))