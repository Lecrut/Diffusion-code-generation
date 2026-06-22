def get_last_key_value(data_dict: dict) -> tuple:
    keys = list(data_dict.keys())
    last_key = keys[-1]
    return last_key, data_dict[last_key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_last_key_value(sample_dict)
    print(result)