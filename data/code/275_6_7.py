def print_values_by_key(dict_list, key):
    for d in dict_list:
        if key in d:
            print(d[key])

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    key_to_print = 'name'
    print_values_by_key(sample_dicts, key_to_print)