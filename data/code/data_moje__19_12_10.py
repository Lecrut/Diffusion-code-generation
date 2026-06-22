import random

def get_random_string(data_tuple, seed_value):
    random.seed(seed_value)
    index = random.randint(0, len(data_tuple) - 1)
    return data_tuple[index]

if __name__ == '__main__':
    sample_data = ("apple", "banana", "cherry", "date", "elderberry")
    sample_seed = 42
    result = get_random_string(sample_data, sample_seed)
    print(result)