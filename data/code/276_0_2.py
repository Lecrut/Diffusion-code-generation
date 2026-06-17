import time
def execute_task(iteration):
    result = 0
    for i in range(1000000):
        result += i
    print(f"Iteration {iteration}: Result calculated.")
    time.sleep(0.001)
    return result
if __name__ == '__main__':
    num_iterations = 5
    for i in range(num_iterations):
        start_time = time.perf_counter()
        result = execute_task(i + 1)
        end_time = time.perf_counter()
        print(f"Finished iteration {i + 1} in {end_time - start_time:.6f} seconds.")