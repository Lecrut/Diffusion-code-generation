def key_exists_in_dicts(key, dict_list):
    return any(key in d for d in dict_list)

if __name__ == '__main__':
    sample_dicts = [{'x': 10}, {'y': 20}, {'z': 30}]
    print(key_exists_in_dicts('y', sample_dicts))
    print(key_exists_in_dicts('w', sample_dicts))