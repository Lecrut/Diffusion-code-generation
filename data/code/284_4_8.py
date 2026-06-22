def reverse_dict_keys(d):
    if not isinstance(d, dict):
        raise ValueError("Input must be a dictionary")
    
    return {k: d[k] for k in reversed(list(d.keys()))}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original dictionary:", sample_dict)
    reversed_dict = reverse_dict_keys(sample_dict)
    print("Reversed dictionary:", reversed_dict)

    sample_dict_2 = {1: 'one', 2: 'two', 3: 'three'}
    print("Original dictionary:", sample_dict_2)
    reversed_dict_2 = reverse_dict_keys(sample_dict_2)
    print("Reversed dictionary:", reversed_dict_2)