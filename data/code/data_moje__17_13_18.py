def get_last_key_value(d):
    for key, value in d.items():
        last_key = key
        last_value = value
    return last_key, last_value

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    result = get_last_key_value(sample_dict)
    print(result)