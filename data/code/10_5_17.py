def get_first_value(data):
    values = list(data.values())
    return values[0]

if __name__ == '__main__':
    sample_dict = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    result = get_first_value(sample_dict)
    print(result)