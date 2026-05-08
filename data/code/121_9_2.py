import time
def benchmark_sort_time(arr1, arr2):
    if len(arr1) < len(arr2):
        larger_arr = arr2
        smaller_arr = arr1
    else:
        larger_arr = arr1
        smaller_arr = arr2
    start_time = time.perf_counter()
    larger_arr.sort()
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    return time_taken
if __name__ == '__main__':
    size1 = 100000
    size2 = 500000
    array1 = list(range(size1))
    array2 = list(range(size2))
    time1 = benchmark_sort_time(array1, array2)
    print(f"Time taken to sort array of size {size1}: {time1:.6f} seconds")
    print(f"Time taken to sort array of size {size2}: {time1:.6f} seconds")