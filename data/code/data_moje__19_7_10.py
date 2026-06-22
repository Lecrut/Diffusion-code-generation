import random

def pick_random(iterable):
    return random.choice(iterable)

if __name__ == '__main__':
    print(pick_random([10, 20, 30, 40, 50]))