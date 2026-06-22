import random

def get_random_value(values):
    if not values:
        raise ValueError("List must not be empty")
    index = random.randrange(len(values))
    return values[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_random_value(sample_list)
    print(result)