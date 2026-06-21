from operator import itemgetter

def sort_dicts_by_key(dicts, key):
    if not all(isinstance(d, dict) for d in dicts):
        raise ValueError("All elements must be dictionaries.")
    if not isinstance(key, str):
        raise ValueError("Key must be a string.")
    
    return sorted(dicts, key=itemgetter(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    sorted_dicts_by_name = sort_dicts_by_key(sample_dicts, 'name')
    print("Sorted by name:", sorted_dicts_by_name)
    
    sorted_dicts_by_age = sort_dicts_by_key(sample_dicts, 'age')
    print("Sorted by age:", sorted_dicts_by_age)