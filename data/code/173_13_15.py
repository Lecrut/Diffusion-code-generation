def validate_lists(keys, values):
    if not (isinstance(keys, list) and isinstance(values, list)):
        raise ValueError("Both inputs must be lists.")
    if len(keys) != len(values):
        raise ValueError("Lists must be of the same length.")

def group_lists(keys, values):
    validate_lists(keys, values)
    return {k: [v] for k, v in zip(keys, values)}

if __name__ == '__main__':
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    print(group_lists(keys, values))