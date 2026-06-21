import numpy as np

def sum_random_integers():
    random_numbers = np.random.randint(0, 100, size=10)
    return random_numbers.sum()

if __name__ == '__main__':
    result = sum_random_integers()
    print(f"Sum of ten random integers: {result}")