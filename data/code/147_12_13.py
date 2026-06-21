def sort_dicts_by_key(dict_list, key):
    if not all(isinstance(item, dict) and key in item for item in dict_list):
        raise ValueError("All items must be dictionaries containing the specified key.")
    
    return sorted(dict_list, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    print("Original list:", data)
    sorted_data = sort_dicts_by_key(data, 'age')
    print("Sorted by age (descending):", sorted_data)