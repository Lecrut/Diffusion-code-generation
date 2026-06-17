import time
def execute_task(iteration):
    result = 0
    for i in range(1000000):
        result += i * iteration
    return result
if __name__ == '__main__':
    iterations_to_run = [1, 2, 3, 4, 5]
    start_time = time.perf_counter()
    total_result = 0
    for iteration in iterations_to_run:
        result = execute_task(iteration)
        total_result += result
    end_time = time.perf_counter()
    print(f"Total Result: {total_result}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")