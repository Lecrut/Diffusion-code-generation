import random

def get_random_value(d):
    if not d:
        return None
    key = random.choice(list(d.keys()))
    return d[key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_random_value(sample_dict)
    print(result)