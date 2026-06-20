def get_nested_value(data, keys):
    for key in keys:
        data = data[key]
    return data

if __name__ == '__main__':
    nested_dict = {
        'a': {
            'b': {
                'c': 42,
                'd': 100
            },
            'e': 50
        },
        'f': 30
    }
    keys = ['a', 'b', 'c']
    result = get_nested_value(nested_dict, keys)
    print(f"Value at {'.'.join(keys)}: {result}")