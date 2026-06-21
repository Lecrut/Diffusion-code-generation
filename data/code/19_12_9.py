import random

def get_random_string(strings, seed):
    random.seed(seed)
    index = random.randint(0, len(strings) - 1)
    return strings[index]

if __name__ == '__main__':
    sample_strings = ("alpha", "beta", "gamma", "delta")
    seed_value = 42
    result = get_random_string(sample_strings, seed_value)
    print(result)