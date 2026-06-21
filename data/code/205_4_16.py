from operator import itemgetter

def sort_dicts_by_key(dicts, key):
    if not all(isinstance(d, dict) and key in d for d in dicts):
        raise ValueError("All items must be dictionaries containing the specified key")
    
    return sorted(dicts, key=itemgetter(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)