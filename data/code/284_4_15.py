def reverse_dict_keys(input_dict):
    return {key: value for key, value in reversed(input_dict.items())}

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original dictionary:", sample_dict)
    reversed_dict = reverse_dict_keys(sample_dict)
    print("Reversed dictionary:", reversed_dict)

    sample_dict_2 = {'x': 10, 'y': 20, 'z': 30}
    print("Original dictionary:", sample_dict_2)
    reversed_dict_2 = reverse_dict_keys(sample_dict_2)
    print("Reversed dictionary:", reversed_dict_2)

    sample_dict_3 = {'m': 5, 'n': 1, 'o': 4, 'p': 2}
    print("Original dictionary:", sample_dict_3)
    reversed_dict_3 = reverse_dict_keys(sample_dict_3)
    print("Reversed dictionary:", reversed_dict_3)