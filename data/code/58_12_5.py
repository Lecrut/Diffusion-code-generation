def safe_first_element(iterable):
    if hasattr(iterable, '__iter__') and not isinstance(iterable, dict):
        try:
            return next(iter(iterable))
        except StopIteration:
            return None
    else:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (40, 50, 60)
    sample_string = "hello"
    sample_dict = {'a': 1, 'b': 2}
    sample_set = {70, 80, 90}
    sample_empty_list = []

    test_values = [
        sample_list,
        sample_tuple,
        sample_string,
        sample_dict,
        sample_set,
        sample_empty_list
    ]

    for value in test_values:
        print(safe_first_element(value))