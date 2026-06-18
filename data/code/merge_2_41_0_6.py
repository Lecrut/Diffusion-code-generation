def count_items(collection):
    if isinstance(collection, dict):
        return len(collection)
    elif isinstance(collection, (list, tuple)):
        return sum(1 for item in collection if not isinstance(item, (dict, list)))
    else:
        raise TypeError("Unsupported collection type")
if __name__ == '__main__':
    sample_list = [1, 2, {'a': 'b'}, ['x', 'y'], None]
    sample_dict = {"key": "value", "nested": {}}
    print(f"List count: {count_items(sample_list)}")
    print(f"Dict count: {count_items(sample_dict)}")