import operator

def sort_dicts_by_key(dict_list, key_name):
    if not all(isinstance(item, dict) and key_name in item for item in dict_list):
        raise ValueError("All items must be dictionaries and contain the specified key")
    
    return sorted(dict_list, key=operator.itemgetter(key_name))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)