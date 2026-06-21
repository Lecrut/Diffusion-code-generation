def validate_objects(objects):
    if not isinstance(objects, list):
        raise ValueError("Input must be a list.")
    for obj in objects:
        if not isinstance(obj, dict):
            raise ValueError("All elements in the list must be dictionaries.")

def sort_objects_by_key(objects, key):
    validate_objects(objects)
    return sorted(objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'title': 'Movie', 'rating': 8.5},
        {'title': 'Series', 'rating': 9.2},
        {'title': 'Documentary', 'rating': 7.8}
    ]
    sorted_data = sort_objects_by_key(sample_data, 'rating')
    print(sorted_data)