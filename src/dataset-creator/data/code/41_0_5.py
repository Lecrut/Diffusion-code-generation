def count_items(data):
    if isinstance(data, list):
        return len(data)
    elif isinstance(data, dict):
        return len(data.keys())
    else:
        raise TypeError("Input must be a list or dictionary.")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_dict = {'a': 'one', 'b': 'two'}
    print(f"List count: {count_items(sample_list)}")
    print(f"Dict count: {count_items(sample_dict)}")