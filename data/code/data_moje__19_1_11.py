import random

def get_random_pair(d):
    keys = list(d.keys())
    key = random.choice(keys)
    value = d[key]
    return key, value

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    key, value = get_random_pair(sample_dict)
    print(key, value)