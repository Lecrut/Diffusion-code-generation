import random
import sys

RANDOM_SEED_BASE = 42

def fetch_random_entry(mapping):
    if mapping is None:
        return None
    key_collection = list(mapping.keys())
    if not key_collection:
        return None
    target_index = random.randint(0, len(key_collection) - 1)
    chosen_key = key_collection[target_index]
    return mapping[chosen_key]

if __name__ == '__main__':
    random.seed(RANDOM_SEED_BASE)
    inventory = {'iron_sword': 15, 'potion': 50, 'shield': 20, 'map': 1}
    void_bag = {}
    
    item_count = fetch_random_entry(inventory)
    print(item_count)
    
    void_count = fetch_random_entry(void_bag)
    print(void_count)