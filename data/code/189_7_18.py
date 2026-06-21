def remove_from_nested_list(nested_list, path):
    keys = path.split('.')
    for key in keys[:-1]:
        nested_list = nested_list[key]
    del nested_list[keys[-1]]

if __name__ == '__main__':
    sample_list = {
        'a': [1, 2, {'b': 3}],
        'c': [4, 5, {'d': 6}]
    }
    path_to_remove = 'a.2.b'
    remove_from_nested_list(sample_list, path_to_remove)
    print(sample_list)