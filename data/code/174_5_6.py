from collections import defaultdict

INITIAL_VALUE = 0

def initialize_and_increment(default_dict, keys):
    for key in keys:
        default_dict[key] += INITIAL_VALUE

if __name__ == '__main__':
    sample_dict = defaultdict(int)
    sample_keys = ['apple', 'banana', 'apple', 'orange', 'banana']
    initialize_and_increment(sample_dict, sample_keys)
    print(dict(sample_dict))