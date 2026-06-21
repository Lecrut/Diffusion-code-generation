def tuple_exists(target_tuple, tuple_list):
    if not isinstance(target_tuple, tuple) or not all((isinstance(item, tuple) for item in tuple_list)):
        raise ValueError('Both target and list items must be tuples.')
    return target_tuple in tuple_list
if __name__ == '__main__':
    sample_tuple = (1, 2)
    sample_list = [(3, 4), (5, 6), (1, 2)]
    result = tuple_exists(sample_tuple, sample_list)
    print(result)