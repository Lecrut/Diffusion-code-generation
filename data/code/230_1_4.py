def filter_dict(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary")
    
    return [(key, value) for key, value in input_dict.items() if value >= 0]

if __name__ == '__main__':
    sample_dict = {'a': -1, 'b': 2, 'c': 3, 'd': -4}
    filtered_result = filter_dict(sample_dict)
    print(filtered_result)