def get_last_key_value_pair(data_dict):
    if not data_dict:
        return None
    keys = list(data_dict.keys())
    last_key = keys[-1]
    return (last_key, data_dict[last_key])

if __name__ == '__main__':
    sample_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
    result = get_last_key_value_pair(sample_dict)
    print(result)