def get_nested_dict_elements(data, *keys):
    if not all((isinstance(key, (str, int)) for key in keys)):
        raise ValueError('All keys must be strings or integers')
    try:
        result = data
        for key in keys:
            result = result[key]
        return result
    except KeyError as e:
        print(f'Key error: {e}')
        raise
if __name__ == '__main__':
    nested_dict = {'a': {'b': {'c': 1, 'd': 2}, 'e': 3}, 'f': 4}
    try:
        print(get_nested_dict_elements(nested_dict, 'a', 'b', 'c'))
        print(get_nested_dict_elements(nested_dict, 'a', 'd'))
    except ValueError as e:
        print(e)