import random

def select_random_key_value(d):
    if not d:
        return None, None
    random_key = random.choice(list(d.keys()))
    return random_key, d[random_key]

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}
    key, value = select_random_key_value(sample_dict)
    print(key, value)