import random

def get_random_string(string_tuple, seed_value):
    random.seed(seed_value)
    index = random.randint(0, len(string_tuple) - 1)
    return string_tuple[index]

if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry", "date", "elderberry")
    seed = 42
    result = get_random_string(sample_tuple, seed)
    print(result)