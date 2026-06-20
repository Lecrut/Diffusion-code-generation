def get_nested_value(data, keys):
    return reduce(lambda d, key: d.get(key), keys, data)

if __name__ == '__main__':
    sample_data = {
        'a': {
            'b': {
                'c': 42
            }
        }
    }
    keys = ['a', 'b', 'c']
    print(get_nested_value(sample_data, keys))