def sort_dicts_by_key(data, key):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("First argument must be a list of dictionaries.")
    
    if not isinstance(key, str) or not key:
        raise ValueError("Second argument must be a non-empty string representing the dictionary key to sort by.")
    
    return sorted(data, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
    print("Original list:", sample_list)
    sorted_list = sort_dicts_by_key(sample_list, 'age')
    print("Sorted list by age in descending order:", sorted_list)