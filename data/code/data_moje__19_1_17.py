import random

def get_random_item(d):
    if not d:
        raise ValueError("Dictionary cannot be empty")
    key = random.choice(list(d.keys()))
    return key, d[key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    key, value = get_random_item(sample_dict)
    print(key, value)