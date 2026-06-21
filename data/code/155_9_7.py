import numpy as np

def sum_random_integers():
    random_integers = np.random.randint(0, 100, size=10)
    return random_integers.sum()

if __name__ == '__main__':
    print(sum_random_integers())