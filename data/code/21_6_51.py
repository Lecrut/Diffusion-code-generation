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
        {'title': 'Book', 'year': 2001},
        {'title': 'Magazine', 'year': 1998},
        {'title': 'Journal', 'year': 2015}
    ]
    try:
        sorted_data = sort_objects_by_key(sample_data, 'year')
        print(sorted_data)
    except ValueError as e:
        print(e)