import random

EMPTY_RESULT = None

def get_random_value(mapping):
    keys = list(mapping.keys())
    if not keys:
        return EMPTY_RESULT
    chosen_key = random.choice(keys)
    return mapping[chosen_key]

if __name__ == '__main__':
    test_data = {'x': 10, 'y': 20, 'z': 30}
    empty_data = {}
    print(get_random_value(test_data))
    print(get_random_value(empty_data))