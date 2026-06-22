import random

def get_string_by_seed(t: tuple, seed: int) -> str:
    random.seed(seed)
    index = random.randrange(len(t))
    return t[index]

if __name__ == '__main__':
    sample_tuple = ('alpha', 'beta', 'gamma', 'delta', 'epsilon')
    sample_seed = 42
    result = get_string_by_seed(sample_tuple, sample_seed)
    print(result)