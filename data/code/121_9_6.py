import time
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
    size1 = 100000
    size2 = 500000
    array1 = list(range(size1))
    array2 = list(range(size2))
    time_taken = benchmark_sort_time(array1, array2)
    print(f"Size of Array 1: {size1}")
    print(f"Size of Array 2: {size2}")
    print(f"Time taken to sort the larger array: {time_taken:.6f} seconds")