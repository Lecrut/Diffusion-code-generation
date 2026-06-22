KEY_TO_PRINT = 'age'

def print_values_by_key(dict_list, key):
    for dictionary in dict_list:
        if key in dictionary:
            print(dictionary[key])

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    print_values_by_key(sample_dicts, KEY_TO_PRINT)