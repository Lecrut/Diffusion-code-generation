def _validate_sequence(data):
    if not hasattr(data, '__len__') or not hasattr(data, '__getitem__'):
        raise TypeError("Data must support indexing and length.")
    if len(data) == 0:
        raise ValueError("Data must not be empty.")

def get_middle_element(collection):
    _validate_sequence(collection)
    center = len(collection) // 2
    return collection[center]

if __name__ == '__main__':
    test_data = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    center_item = get_middle_element(test_data)
    print(center_item)