import random

def pick_random(it):
    return random.choice(it)

if __name__ == '__main__':
    print(pick_random([1, 2, 3]))