def get_last_inserted_pair(data_dict):
    if not data_dict:
        return None
    last_key = next(reversed(data_dict))
    return (last_key, data_dict[last_key])

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    result = get_last_inserted_pair(sample_dict)
    print(result)