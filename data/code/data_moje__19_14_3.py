import random

def get_random_value(d):
    if not d:
        return None
    keys = list(d.keys())
    key = random.choice(keys)
    return d[key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_random_value(sample_dict)
    print(result)
    empty_dict = {}
    empty_result = get_random_value(empty_dict)
    print(empty_result)