def print_values_by_key(dict_list, key):
    for dictionary in dict_list:
        if key in dictionary:
            print(dictionary[key])

if __name__ == '__main__':
    sample_dicts = [
        {'title': 'Python', 'language': 'English'},
        {'title': 'Java', 'language': 'English'},
        {'title': 'C++', 'language': 'C++'}
    ]
    key_to_print = 'language'
    print_values_by_key(sample_dicts, key_to_print)