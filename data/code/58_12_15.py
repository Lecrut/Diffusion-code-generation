def safe_first_element(iterable):
    try:
        iterator = iter(iterable)
        first_item = next(iterator)
        return first_item
    except (TypeError, StopIteration):
        return None

if __name__ == '__main__':
    sample_list = [100, 200, 300]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "world"
    sample_dict = {'key1': 'value1', 'key2': 'value2'}
    sample_set = {4, 5, 6}
    sample_empty_list = []

    print(safe_first_element(sample_list))
    print(safe_first_element(sample_tuple))
    print(safe_first_element(sample_string))
    print(safe_first_element(sample_dict))  # This will print None
    print(safe_first_element(sample_set))   # This will print None
    print(safe_first_element(sample_empty_list))  # This will print None