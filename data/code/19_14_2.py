import random

def get_random_value(data):
    if not data:
        return None
    keys = list(data.keys())
    random_key = random.choice(keys)
    return data[random_key]

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    print(get_random_value(sample_dict))
    print(get_random_value({}))