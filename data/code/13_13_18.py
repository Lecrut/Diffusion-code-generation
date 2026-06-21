def get_dict_value(dictionary, key, default=None):
    return dictionary.get(key, default)

if __name__ == '__main__':
    sample_dict = {'name': 'Alice', 'age': 30}
    print(get_dict_value(sample_dict, 'name'))
    print(get_dict_value(sample_dict, 'city', 'Unknown'))