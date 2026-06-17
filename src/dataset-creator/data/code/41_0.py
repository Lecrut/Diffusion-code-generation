def count_items(collection):
    if isinstance(collection, list):
        return len(collection)
    elif isinstance(collection, dict):
        return len(collection.keys())
    else:
        raise TypeError("Input must be a list or dictionary.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_dict = {'a': 'one', 'b': 'two'}
    print(f"List count: {count_items(sample_list)}")
    print(f"Dict count: {count_items(sample_dict)}")