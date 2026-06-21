def sort_dicts_by_key(data, key):
    if not all(isinstance(item, dict) and key in item for item in data):
        raise ValueError("All items must be dictionaries containing the specified key")
    
    return sorted(data, key=lambda x: x[key], reverse=True)

if __name__ == '__main__':
    sample_list = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    print("Original list:", sample_list)
    sorted_list = sort_dicts_by_key(sample_list, 'age')
    print("Sorted list by age (descending):", sorted_list)