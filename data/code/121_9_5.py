import time
import random
def benchmark_sort_time(arr1, arr2):
    if len(arr1) < len(arr2):
        arr_smaller = arr1
        arr_larger = arr2
    else:
        arr_smaller = arr2
        arr_larger = arr1
    start_time = time.perf_counter()
    arr_larger.sort()
    end_time = time.perf_counter()
    return end_time - start_time
if __name__ == '__main__':
    N1 = 100000
    N2 = 500000
    arr1 = [random.randint(0, 1000000) for _ in range(N1)]
    arr2 = [random.randint(0, 1000000) for _ in range(N2)]
    time_taken = benchmark_sort_time(arr1, arr2)
    print(f"Size of Array 1: {N1}")
    print(f"Size of Array 2: {N2}")
    print(f"Time taken to sort the larger array: {time_taken:.6f} seconds")