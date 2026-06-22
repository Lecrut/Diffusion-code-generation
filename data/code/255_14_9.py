import random
import time

def find_max_value(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample_sizes = [10**3, 10**4, 10**5, 10**6]
    for size in sample_sizes:
        numbers = [random.randint(0, 1000) for _ in range(size)]
        start_time = time.time()
        max_value = find_max_value(numbers)
        end_time = time.time()
        print(f"Size: {size}, Max Value: {max_value}, Time: {end_time - start_time:.6f} seconds")