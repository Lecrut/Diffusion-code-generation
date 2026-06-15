import time
def concatenate_lists(list_a, list_b):
    return list_a + list_b
if __name__ == '__main__':
    list_a = list(range(1000000))
    list_b = list(range(2000000))
    start_time = time.perf_counter()
    result = concatenate_lists(list_a, list_b)
    end_time = time.perf_counter()
    print(f"Result length: {len(result)}")
    print(f"Time taken: {(end_time - start_time):.6f} seconds")