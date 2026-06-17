import time
def execute_task(iteration):
    result = 0
    for i in range(1000000):
        result += i * iteration
    return result
if __name__ == '__main__':
    iterations = [1, 2, 3, 4, 5]
    total_sum = 0
    start_time = time.perf_counter()
    for k in iterations:
        result = execute_task(k)
        total_sum += result
    end_time = time.perf_counter()
    print(f"Total sum of results: {total_sum}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")