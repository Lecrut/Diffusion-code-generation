import random
import time

def find_max_value(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_sizes = [10**3, 10**4, 10**5, 10**6]
    results = []
    for size in sample_sizes:
        lst = [random.randint(0, size) for _ in range(size)]
        start_time = time.time()
        max_value = find_max_value(lst)
        end_time = time.time()
        time_taken = end_time - start_time
        results.append((size, max_value, time_taken))
    for result in results:
        print(f"List size: {result[0]}, Max value: {result[1]}, Time taken: {result[2]:.6f} seconds")