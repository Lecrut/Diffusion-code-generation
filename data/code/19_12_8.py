import random

def select_random_string(data, seed):
    random.seed(seed)
    index = random.randint(0, len(data) - 1)
    return data[index]

if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry", "date")
    sample_seed = 42
    result = select_random_string(sample_tuple, sample_seed)
    print(result)