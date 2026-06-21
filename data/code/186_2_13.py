from operator import itemgetter

def sort_dicts_by_key(dict_list, key):
    if not all(isinstance(d, dict) for d in dict_list):
        raise ValueError("All elements must be dictionaries.")
    if not isinstance(key, str) or not key:
        raise ValueError("Key must be a non-empty string.")
    
    return sorted(dict_list, key=itemgetter(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'name')
    print(sorted_dicts)