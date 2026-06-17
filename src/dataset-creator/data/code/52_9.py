import timeit
def check_last_slice(arr):
    return arr[-1]
def check_last_index(arr):
    n = len(arr)
    if n == 0:
        raise IndexError("Empty array")
    return arr[n - 1]
if __name__ == '__main__':
    data = list(range(1_000_000)) * 10
    slice_time = timeit.timeit('check_last_slice(data)', globals=globals(), number=10)
    index_time = timeit.timeit('check_last_index(data)', globals=globals(), number=10)
    print(f"Slice method total: {slice_time:.4f}s")
    print(f"Index method total: {index_time:.4f}s")