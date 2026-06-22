import random

def get_random_item(d):
    keys = list(d.keys())
    key = random.choice(keys)
    return key, d[key]

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    key, value = get_random_item(sample_dict)
    print(key, value)