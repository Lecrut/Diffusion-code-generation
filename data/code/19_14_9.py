import random

def fetch_random_value(source_map):
    key_collection = list(source_map.keys())
    if len(key_collection) == 0:
        return None
    random_index = random.randint(0, len(key_collection) - 1)
    chosen_key = key_collection[random_index]
    return source_map[chosen_key]

if __name__ == '__main__':
    sample_data = {'alpha': 10, 'beta': 20, 'gamma': 30, 'delta': 40}
    output = fetch_random_value(sample_data)
    print(output)
    print(fetch_random_value({}))