import operator

def sort_dicts_by_key(dict_list, key):
    if not all(isinstance(item, dict) for item in dict_list):
        raise ValueError("All elements must be dictionaries")
    if key not in dict_list[0]:
        raise KeyError(f"Key '{key}' not found in dictionaries")
    
    return sorted(dict_list, key=operator.itemgetter(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    sorted_by_age = sort_dicts_by_key(sample_dicts, 'age')
    print("Sorted by age:")
    for d in sorted_by_age:
        print(d)