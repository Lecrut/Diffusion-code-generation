import operator

def sort_dicts_by_key(dict_list, key):
    if not all(isinstance(d, dict) for d in dict_list):
        raise ValueError("All elements in the list must be dictionaries.")
    if key not in dict_list[0]:
        raise KeyError(f"Key '{key}' not found in dictionary keys.")
    return sorted(dict_list, key=operator.itemgetter(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)