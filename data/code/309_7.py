def find_sum_loop(data):
    total = 0
    for item in data:
        total += item
    return total
def find_sum_builtin(data):
    return sum(data)
if __name__ == '__main__':
    import time
    import random
    LIST_SIZE = 10**6
    SAMPLE_DATA = [random.randint(1, 1000) for _ in range(LIST_SIZE)]
    print(f"List size: {LIST_SIZE}")
    start_time_loop = time.perf_counter()
    result_loop = find_sum_loop(SAMPLE_DATA)
    end_time_loop = time.perf_counter()
    time_loop = end_time_loop - start_time_loop
    start_time_builtin = time.perf_counter()
    result_builtin = find_sum_builtin(SAMPLE_DATA)
    end_time_builtin = time.perf_counter()
    time_builtin = end_time_builtin - start_time_builtin
    print(f"Result (Loop): {result_loop}")
    print(f"Time (Loop): {time_loop:.6f} seconds")
    print("-" * 30)
    print(f"Result (Built-in sum()): {result_builtin}")
    print(f"Time (Built-in sum()): {time_builtin:.6f} seconds")