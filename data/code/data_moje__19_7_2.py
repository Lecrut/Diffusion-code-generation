import random

def pick_random_item(iterable):
    return random.choice(list(iterable))

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(pick_random_item(sample_data))