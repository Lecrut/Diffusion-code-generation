import random

def get_random_value(index_range, values):
    index = random.choice(list(index_range))
    return values[index]

if __name__ == '__main__':
    sample_range = range(5, 15)
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = get_random_value(sample_range, sample_list)
    print(result)