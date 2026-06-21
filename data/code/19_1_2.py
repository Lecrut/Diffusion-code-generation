import random

def get_random_item(d):
    if not d:
        raise ValueError("Dictionary is empty")
    key = random.choice(list(d.keys()))
    return key, d[key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    result_key, result_value = get_random_item(sample_dict)
    print(f"Key: {result_key}, Value: {result_value}")