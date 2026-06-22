import random

def get_random_item(dictionary):
    keys = list(dictionary.keys())
    key = random.choice(keys)
    return key, dictionary[key]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_random_item(sample_dict)
    print(result)