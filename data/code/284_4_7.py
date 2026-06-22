def reverse_dict(input_dict):
    return {key: value for key, value in reversed(list(input_dict.items()))}

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    print("Original dict:", sample_dict1)
    reversed_dict1 = reverse_dict(sample_dict1)
    print("Reversed dict:", reversed_dict1)
    sample_dict2 = {'apple': 10, 'banana': 5, 'cherry': 20}
    print("Original dict:", sample_dict2)
    reversed_dict2 = reverse_dict(sample_dict2)
    print("Reversed dict:", reversed_dict2)
    sample_dict3 = {1: 'one', 2: 'two', 3: 'three'}
    print("Original dict:", sample_dict3)
    reversed_dict3 = reverse_dict(sample_dict3)
    print("Reversed dict:", reversed_dict3)