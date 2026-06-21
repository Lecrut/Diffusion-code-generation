import random

def get_random_string_from_tuple(string_tuple, seed):
    random.seed(seed)
    index = random.randint(0, len(string_tuple) - 1)
    return string_tuple[index]

if __name__ == '__main__':
    sample_tuple = ('alpha', 'beta', 'gamma', 'delta')
    sample_seed = 42
    result = get_random_string_from_tuple(sample_tuple, sample_seed)
    print(result)