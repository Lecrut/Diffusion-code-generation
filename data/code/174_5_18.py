from collections import defaultdict

def increment_keys(default_dict, keys):
    for key in keys:
        default_dict[key] += 1

if __name__ == '__main__':
    default_dict = defaultdict(int)
    keys_to_increment = ['a', 'b', 'c', 'a']
    increment_keys(default_dict, keys_to_increment)
    print(dict(default_dict))