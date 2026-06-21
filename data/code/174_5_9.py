from collections import defaultdict

def initialize_default_dict(keys):
    if not isinstance(keys, list) or not all(isinstance(key, str) for key in keys):
        raise ValueError("Keys must be a list of strings")
    
    default_dict = defaultdict(int)
    return default_dict

def increment_keys(default_dict, keys):
    for key in keys:
        default_dict[key] += 1
    return default_dict

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'apple', 'orange', 'banana']
    initialized_dict = initialize_default_dict(sample_keys)
    incremented_dict = increment_keys(initialized_dict, sample_keys)
    print(dict(incremented_dict))