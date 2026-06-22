def sort_objects_by_key(objects, key):
    if not all(isinstance(obj, dict) for obj in objects):
        raise ValueError("All elements must be dictionaries.")
    return sorted(objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'title': 'Book', 'year': 2001},
        {'title': 'Magazine', 'year': 1998},
        {'title': 'Journal', 'year': 2015}
    ]
    sorted_data = sort_objects_by_key(sample_data, 'year')
    print(sorted_data)