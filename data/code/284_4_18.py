def reverse_dict_keys(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary")
    
    return {key: input_dict[key] for key in reversed(list(input_dict.keys()))}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original dict:", sample_dict)
    reversed_dict = reverse_dict_keys(sample_dict)
    print("Reversed dict:", reversed_dict)