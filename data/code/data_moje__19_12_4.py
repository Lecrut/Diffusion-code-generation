import random

def select_random_string(string_tuple, seed_value):
    random.seed(seed_value)
    index = random.randint(0, len(string_tuple) - 1)
    return string_tuple[index]

if __name__ == '__main__':
    sample_strings = ("apple", "banana", "cherry", "date", "elderberry")
    sample_seed = 42
    result = select_random_string(sample_strings, sample_seed)
    print(result)