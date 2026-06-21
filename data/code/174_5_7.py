from collections import defaultdict

def increment_keys(default_dict, keys):
    for key in keys:
        default_dict[key] += 1
    return default_dict

if __name__ == '__main__':
    sample_dict = defaultdict(int)
    sample_keys = ['a', 'b', 'c', 'a', 'b']
    result = increment_keys(sample_dict, sample_keys)
    print(result)