def print_values_by_key(dict_list, key):
    for dictionary in dict_list:
        if key in dictionary:
            print(dictionary[key])

if __name__ == '__main__':
    sample_dicts = [
        {'city': 'New York', 'population': 8419000},
        {'city': 'Los Angeles', 'population': 3971000},
        {'city': 'Chicago', 'population': 2716000}
    ]
    key_to_print = 'population'
    print_values_by_key(sample_dicts, key_to_print)