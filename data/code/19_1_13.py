import random

def get_random_key_value(d):
    keys = list(d.keys())
    key = random.choice(keys)
    return key, d[key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    k, v = get_random_key_value(sample_dict)
    print(f"Key: {k}, Value: {v}")