import time
def benchmark_sort_time(arr1, arr2):
    start_time1 = time.perf_counter()
    arr1.sort()
    end_time1 = time.perf_counter()
    time1 = end_time1 - start_time1
    start_time2 = time.perf_counter()
    arr2.sort()
    end_time2 = time.perf_counter()
    time2 = end_time2 - start_time2
    return time1, time2
if __name__ == '__main__':
    size1 = 100000
    size2 = 500000
    arr1 = list(range(size1))
    arr2 = list(range(size2))
    time1, time2 = benchmark_sort_time(arr1, arr2)
    print(f"Size 1: {size1}, Time taken: {time1:.6f} seconds")
    print(f"Size 2: {size2}, Time taken: {time2:.6f} seconds")