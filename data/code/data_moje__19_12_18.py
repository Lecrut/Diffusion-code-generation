import random

def get_random_element(input_tuple, seed_val):
    if not input_tuple:
        return None
    random.seed(seed_val)
    count = len(input_tuple)
    selected_index = random.randrange(count)
    return input_tuple[selected_index]

if __name__ == '__main__':
    words = ("dog", "cat", "bird", "fish")
    rng_seed = 100
    picked_word = get_random_element(words, rng_seed)
    print(picked_word)