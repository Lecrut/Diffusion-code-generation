import random
import time

def find_max_value(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_sizes = [10**3, 10**4, 10**5, 10**6]
    for size in sample_sizes:
        lst = [random.randint(0, size) for _ in range(size)]
        start_time = time.time()
        max_value = find_max_value(lst)
        end_time = time.time()
        print(f"List size: {size}, Max value: {max_value}, Time taken: {end_time - start_time:.6f} seconds")