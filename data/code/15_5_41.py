def validate_input(input_dict, key1, key2):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary.")
    if key1 not in input_dict:
        raise KeyError(f"Key '{key1}' is missing from the dictionary.")
    if key2 not in input_dict:
        raise KeyError(f"Key '{key2}' is missing from the dictionary.")

def check_keys_identical(input_dict, key1, key2):
    validate_input(input_dict, key1, key2)
    return {key1: input_dict[key1] == input_dict.get(key2)}

if __name__ == '__main__':
    sample_dict = {'one': 30, 'two': 60, 'three': 30}
    try:
        result = check_keys_identical(sample_dict, 'one', 'three')
        print(result)
    except (ValueError, KeyError) as e:
        print(e)