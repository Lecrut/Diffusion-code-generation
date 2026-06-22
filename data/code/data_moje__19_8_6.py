import random

def get_random_element(index_range, values):
    index = random.choice(list(index_range))
    return values[index]

if __name__ == '__main__':
    sample_range = range(5, 10)
    sample_list = [100, 200, 300, 400, 500, 600, 700]
    result = get_random_element(sample_range, sample_list)
    print(result)