import numpy as np

def sum_random_numbers():
    numbers = np.random.randint(-100, 100, size=10)
    return numbers.sum()

if __name__ == '__main__':
    result = sum_random_numbers()
    print(f"Sum of random numbers: {result}")