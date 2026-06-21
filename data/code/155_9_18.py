import numpy as np

def sum_random_numbers():
    random_numbers = np.random.randint(1, 100, size=10)
    return random_numbers.sum()

if __name__ == '__main__':
    result = sum_random_numbers()
    print(f"Sum of random numbers: {result}")