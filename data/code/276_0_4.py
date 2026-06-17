import time
def execute_task(iteration):
    result = 0
    for i in range(1000000):
        result += i
    time.sleep(0.01)
    return result + iteration
if __name__ == '__main__':
    num_iterations = 5
    start_time = time.perf_counter()
    for i in range(num_iterations):
        execute_task(i)
    end_time = time.perf_counter()
    print(f"Total execution time: {end_time - start_time}")