def print_values_by_key(dict_list, key):
    if not all(isinstance(item, dict) for item in dict_list):
        raise ValueError("All elements in the list must be dictionaries.")
    if not isinstance(key, str):
        raise ValueError("The key must be a string.")

    for dictionary in dict_list:
        if key in dictionary:
            print(dictionary[key])

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    key_to_print = 'name'
    print_values_by_key(sample_dicts, key_to_print)