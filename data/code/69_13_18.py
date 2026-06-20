def get_nested_value(data, indices):
    for index in indices:
        data = data[index]
    return data

if __name__ == '__main__':
    sample_data = {
        'a': {
            'b': {
                'c': 42
            }
        }
    }
    indices = ['a', 'b', 'c']
    print(get_nested_value(sample_data, indices))