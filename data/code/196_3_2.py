import time
def optimized_concatenate(list_a, list_b):
    return list_a + list_b
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    start_time = time.perf_counter()
    result = optimized_concatenate(list_a, list_b)
    end_time = time.perf_counter()
    print(f"Result: {result}")
    print(f"Time taken: {(end_time - start_time)}")