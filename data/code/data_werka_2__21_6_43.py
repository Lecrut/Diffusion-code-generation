def sort_objects_by_key(objects, key):
    if not isinstance(objects, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(obj, dict) for obj in objects):
        raise ValueError("All elements in the list must be dictionaries.")
    if not isinstance(key, str):
        raise ValueError("Key must be a string.")
    
    return sorted(objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'model': 'Tesla Model S', 'year': 2020},
        {'model': 'Ford Mustang', 'year': 1965},
        {'model': 'Chevrolet Camaro', 'year': 2018}
    ]
    sorted_data = sort_objects_by_key(sample_data, 'year')
    print(sorted_data)