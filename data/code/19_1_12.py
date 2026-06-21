import random

def get_random_key_value_pair(data):
    if not data:
        raise ValueError("Dictionary is empty")
    items = list(data.items())
    return random.choice(items)

if __name__ == '__main__':
    sample_dict = {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 2}
    key, value = get_random_key_value_pair(sample_dict)
    print(key, value)