def sort_objects_by_key(objects, key):
    if not isinstance(objects, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(obj, dict) for obj in objects):
        raise ValueError("All elements must be dictionaries.")
    return sorted(objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    key_to_sort_by = 'age'
    sorted_data = sort_objects_by_key(sample_data, key_to_sort_by)
    print(sorted_data)