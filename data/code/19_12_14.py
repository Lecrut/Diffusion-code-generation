import random

def get_random_string_by_seed(strings, seed):
    random.seed(seed)
    index = random.randint(0, len(strings) - 1)
    return strings[index]

if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry", "date")
    sample_seed = 42
    result = get_random_string_by_seed(sample_tuple, sample_seed)
    print(result)