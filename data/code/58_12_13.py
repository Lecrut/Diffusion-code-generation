def safe_first_element(iterable):
    try:
        return next(iter(iterable))
    except TypeError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (40, 50, 60)
    sample_string = "hello"
    sample_dict = {'a': 1, 'b': 2}
    sample_set = {70, 80, 90}
    sample_empty_list = []
    sample_non_iterable = 123

    print(safe_first_element(sample_list))
    print(safe_first_element(sample_tuple))
    print(safe_first_element(sample_string))
    print(safe_first_element(sample_dict))  # This will print None
    print(safe_first_element(sample_set))   # This will print None
    print(safe_first_element(sample_empty_list))  # This will print None
    print(safe_first_element(sample_non_iterable))  # This will print None