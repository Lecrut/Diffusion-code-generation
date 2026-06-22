import random

def pick_random(iterable):
    return random.choice(iterable)

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    print(pick_random(sample))