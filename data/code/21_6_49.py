def sort_objects_by_key(objects, key):
    if not isinstance(objects, list) or not all(isinstance(obj, dict) for obj in objects):
        raise ValueError("Input must be a list of dictionaries.")
    if not isinstance(key, str):
        raise ValueError("Key must be a string.")
    
    return sorted(objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'model': 'Tesla Model S', 'year': 2020},
        {'model': 'Honda Accord', 'year': 1995},
        {'model': 'Ford Mustang', 'year': 2018}
    ]
    sorted_data = sort_objects_by_key(sample_data, 'year')
    print(sorted_data)