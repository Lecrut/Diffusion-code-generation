import random

def get_random_string(items, seed_value):
    random.seed(seed_value)
    index = random.randint(0, len(items) - 1)
    return items[index]

if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry", "date", "elderberry")
    sample_seed = 42
    result = get_random_string(sample_tuple, sample_seed)
    print(result)