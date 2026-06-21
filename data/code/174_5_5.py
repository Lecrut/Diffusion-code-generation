from collections import defaultdict

def increment_keys(default_dict, keys):
    for key in keys:
        default_dict[key] += 1

if __name__ == '__main__':
    sample_dict = defaultdict(int)
    sample_keys = ['a', 'b', 'c', 'a', 'b']
    increment_keys(sample_dict, sample_keys)
    print(dict(sample_dict))