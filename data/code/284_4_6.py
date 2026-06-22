def reverse_dict_keys(d):
    if not isinstance(d, dict):
        raise ValueError("Input must be a dictionary")
    return {key: d[key] for key in reversed(d)}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original dictionary:", sample_dict)
    reversed_dict = reverse_dict_keys(sample_dict)
    print("Reversed dictionary:", reversed_dict)