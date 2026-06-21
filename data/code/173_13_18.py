def validate_lists(keys, values):
    if not all(isinstance(k, str) for k in keys):
        raise ValueError("All keys must be strings")
    if len(keys) != len(values):
        raise ValueError("Keys and values lists must have the same length")

def group_lists(keys, values):
    validate_lists(keys, values)
    return {k: [v] for k, v in zip(keys, values)}

if __name__ == '__main__':
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    grouped_dict = group_lists(keys, values)
    print(grouped_dict)