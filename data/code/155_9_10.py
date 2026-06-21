import numpy as np

def sum_random_integers():
    random_numbers = np.random.randint(1, 100, 10)
    return random_numbers.sum()

if __name__ == '__main__':
    result = sum_random_integers()
    print(f"Sum of 10 random integers: {result}")