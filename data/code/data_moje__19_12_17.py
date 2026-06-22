import random

def get_random_string_at_seed(string_tuple, seed):
    random.seed(seed)
    index = random.randint(0, len(string_tuple) - 1)
    return string_tuple[index]

if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry", "date", "elderberry")
    sample_seed = 42
    result = get_random_string_at_seed(sample_tuple, sample_seed)
    print(result)