import random

def select_random_pair(data):
    if not data:
        raise ValueError("Dictionary cannot be empty")
    keys = list(data.keys())
    random_key = random.choice(keys)
    random_value = data[random_key]
    return random_key, random_value

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}
    key, value = select_random_pair(sample_dict)
    print(key)
    print(value)