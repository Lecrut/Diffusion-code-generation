def check_keys_identical(input_dict, key1, key2):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary.")
    if key1 not in input_dict or key2 not in input_dict:
        raise KeyError(f"One or both keys ({key1}, {key2}) are missing from the dictionary.")
    return {key1: input_dict[key1] == input_dict[key2]}

if __name__ == '__main__':
    sample_dict = {'alpha': 3, 'beta': 6, 'gamma': 3}
    try:
        result = check_keys_identical(sample_dict, 'alpha', 'gamma')
        print(result)
    except (ValueError, KeyError) as e:
        print(e)