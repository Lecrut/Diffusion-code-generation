import random
import time

def find_max_value(lst):
    return max(lst)

if __name__ == '__main__':
    sample_sizes = [10**3, 10**4, 10**5, 10**6]
    for size in sample_sizes:
        lst = [random.randint(0, 10**9) for _ in range(size)]
        start_time = time.time()
        max_value = find_max_value(lst)
        end_time = time.time()
        print(f"List size: {size}, Max value: {max_value}, Time taken: {end_time - start_time:.6f} seconds")