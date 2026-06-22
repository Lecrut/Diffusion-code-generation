import random

EMPTY_DICT_RETURN = None
DEFAULT_SEED = None

def get_random_value(dictionary):
    if not dictionary:
        return EMPTY_DICT_RETURN
    key_list = list(dictionary.keys())
    chosen_key = random.choice(key_list)
    return dictionary[chosen_key]

if __name__ == '__main__':
    if DEFAULT_SEED is not None:
        random.seed(DEFAULT_SEED)
    
    inventory = {'sword': 15, 'shield': 20, 'potion': 5, 'map': 10, 'ring': 100}
    void_inventory = {}
    
    picked_item_value = get_random_value(inventory)
    empty_check = get_random_value(void_inventory)
    
    print(picked_item_value)
    print(empty_check)