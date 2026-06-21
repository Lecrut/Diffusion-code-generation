from operator import itemgetter

def sort_dicts_by_key(dict_list, key):
    if not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
        raise ValueError("Input must be a list of dictionaries.")
    
    if not key:
        raise ValueError("Key cannot be empty.")

    return sorted(dict_list, key=itemgetter(key))

if __name__ == '__main__':
    sample1 = [{'name': 'apple', 'price': 1}, {'name': 'banana', 'price': 2}]
    print("Sample 1:")
    print(sort_dicts_by_key(sample1, 'name'))

    sample2 = [{'value': 3.14}, {'value': 1.618}, {'value': 2.718}]
    print("\nSample 2:")
    print(sort_dicts_by_key(sample2, 'value'))