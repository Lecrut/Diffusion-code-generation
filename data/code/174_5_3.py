from collections import defaultdict

def initialize_and_increment(default_dict, keys):
    if not isinstance(keys, list) or not all(isinstance(key, str) for key in keys):
        raise ValueError("Keys must be a list of strings")
    
    for key in keys:
        default_dict[key] += 1

if __name__ == '__main__':
    sample_dict = defaultdict(int)
    sample_keys = ['apple', 'banana', 'apple', 'orange', 'banana']
    initialize_and_increment(sample_dict, sample_keys)
    print(dict(sample_dict))