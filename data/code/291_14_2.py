import time
def create_long_string(size):
    return "a" * size
SIZE = 1000000
str1 = create_long_string(SIZE)
str2 = create_long_string(SIZE)
def compare_direct(s1, s2):
    return len(s1) == len(s2)
def compare_len_builtin(s1, s2):
    return len(s1) == len(s2)
def compare_manual_iteration(s1, s2):
    count1 = 0
    for _ in range(len(s1)):
        count1 += 1
    count2 = 0
    for _ in range(len(s2)):
        count2 += 1
    return count1 == count2
def benchmark():
    times = {}
    start_time = time.perf_counter()
    result_direct = compare_direct(str1, str2)
    end_time = time.perf_counter()
    times['Direct Comparison'] = end_time - start_time
    start_time = time.perf_counter()
    result_builtin = compare_len_builtin(str1, str2)
    end_time = time.perf_counter()
    times['Built-in len()'] = end_time - start_time
    start_time = time.perf_counter()
    result_manual = compare_manual_iteration(str1, str2)
    end_time = time.perf_counter()
    times['Manual Iteration'] = end_time - start_time
    print(f"String Length: {SIZE}")
    print("--- Benchmark Results ---")
    for method, duration in times.items():
        print(f"{method}: {duration:.6f} seconds")
if __name__ == '__main__':
    benchmark()