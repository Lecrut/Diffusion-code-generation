import random

def pick_random_pair(d):
    if not d:
        raise ValueError("Dictionary must not be empty")
    keys = list(d.keys())
    key = random.choice(keys)
    return key, d[key]

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    result = pick_random_pair(sample_dict)
    print(result)