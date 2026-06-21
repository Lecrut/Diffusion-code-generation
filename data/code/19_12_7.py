import random

def get_random_string_from_tuple(strings_tuple, seed_value):
    random.seed(seed_value)
    index = random.randint(0, len(strings_tuple) - 1)
    return strings_tuple[index]

if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry", "date", "elderberry")
    sample_seed = 42
    result = get_random_string_from_tuple(sample_tuple, sample_seed)
    print(result)