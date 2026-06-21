import random

def pick_random_string(strings, seed):
    random.seed(seed)
    index = random.randint(0, len(strings) - 1)
    return strings[index]

if __name__ == '__main__':
    sample_strings = ("apple", "banana", "cherry", "date", "elderberry")
    sample_seed = 42
    result = pick_random_string(sample_strings, sample_seed)
    print(result)