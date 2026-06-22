import random

INDEX_OFFSET = 0

def select_string_by_seed(string_tuple, seed_value):
    random.seed(seed_value)
    upper_bound = len(string_tuple)
    index = random.randrange(0, upper_bound)
    return string_tuple[index]

if __name__ == '__main__':
    data = ("zest", "fig", "kiwi", "lime")
    seed = 100
    value = select_string_by_seed(data, seed)
    print(value)