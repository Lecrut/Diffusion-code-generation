def key_exists_in_dicts(key, dict_list):
    return any(key in d for d in dict_list)

if __name__ == '__main__':
    sample_dicts = [{'x': 10}, {'y': 20}, {'z': 30}]
    search_key = 'y'
    result = key_exists_in_dicts(search_key, sample_dicts)
    print(result)