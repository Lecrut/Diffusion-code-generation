import random

def get_random_value(d):
    if not d:
        return None
    random_key = random.choice(list(d.keys()))
    return d[random_key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(get_random_value(sample_dict))
    print(get_random_value({}))