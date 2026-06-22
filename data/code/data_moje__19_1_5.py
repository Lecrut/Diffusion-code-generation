import random

def select_random_pair(d):
    keys = list(d.keys())
    if not keys:
        return None, None
    key = random.choice(keys)
    value = d[key]
    return key, value

if __name__ == '__main__':
    sample_dict = {
        'apple': 1,
        'banana': 2,
        'cherry': 3,
        'date': 4
    }
    k, v = select_random_pair(sample_dict)
    print(k, v)