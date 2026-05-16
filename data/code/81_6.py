import time
def calculate_elapsed_time(start_time, end_time):
    elapsed = end_time - start_time
    return elapsed
if __name__ == '__main__':
    start = time.time()
    time.sleep(0.5)
    end = time.time()
    result = calculate_elapsed_time(start, end)
    print(f"Elapsed time: {result}")