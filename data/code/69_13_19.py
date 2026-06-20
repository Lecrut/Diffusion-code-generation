def get_nested_value(data, keys):
    for key in keys:
        data = data[key]
    return data

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