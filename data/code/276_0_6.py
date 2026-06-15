import time
def execute_task(iteration):
    result = 0
    for i in range(1000000):
        result += i
    time.sleep(0.001)
    return result
if __name__ == '__main__':
    num_iterations = 5
    start_time = time.perf_counter()
    for i in range(num_iterations):
        result = execute_task(i)
        pass