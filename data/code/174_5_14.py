from collections import defaultdict

def initialize_and_increment(default_dict, keys):
    for key in keys:
        default_dict[key] += 1

if __name__ == '__main__':
    sample_dict = defaultdict(int)
    sample_keys = ['red', 'blue', 'green', 'red', 'blue']
    initialize_and_increment(sample_dict, sample_keys)
    print(dict(sample_dict))