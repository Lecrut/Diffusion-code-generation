import numpy as np

def calculate_sum():
    numbers = np.random.randint(-100, 100, size=10)
    return numbers.sum()

if __name__ == '__main__':
    result = calculate_sum()
    print(f"Sum of random integers: {result}")