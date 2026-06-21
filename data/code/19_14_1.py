import random

def get_random_value(data):
    keys = list(data.keys())
    if not keys:
        return None
    key = random.choice(keys)
    return data[key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_random_value(sample_dict)
    print(result)