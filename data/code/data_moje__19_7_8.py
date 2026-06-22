import random

def pick_random_item(iterable):
    return random.choice(iterable)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(pick_random_item(sample_data))