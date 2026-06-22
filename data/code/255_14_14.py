import random
import time

def find_max_value(lst):
    return max(lst)

if __name__ == '__main__':
    sample_sizes = [10**i for i in range(1, 6)]
    for size in sample_sizes:
        lst = [random.randint(-10**9, 10**9) for _ in range(size)]
        start_time = time.time()
        max_value = find_max_value(lst)
        end_time = time.time()
        print(f"List size: {size}, Max value: {max_value}, Time taken: {end_time - start_time:.6f} seconds")