from collections import defaultdict

def initialize_and_increment(default_dict, keys):
    for key in keys:
        default_dict[key] += 1

if __name__ == '__main__':
    INIT_VALUE = 0
    sample_dict = defaultdict(lambda: INIT_VALUE)
    sample_keys = ['apple', 'banana', 'apple', 'orange', 'banana']
    initialize_and_increment(sample_dict, sample_keys)
    print(dict(sample_dict))