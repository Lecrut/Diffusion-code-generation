import time
def check_presence_efficiently(target_list, master_list):
    master_set = set(master_list)
    for item in target_list:
        if item in master_set:
            return True
    return False
if __name__ == '__main__':
    target = [1, 5, 9, 12]
    master = list(range(1, 100))
    start_time = time.perf_counter()
    result = check_presence_efficiently(target, master)
    end_time = time.perf_counter()
    print(result)
    print(f"Execution time: {end_time - start_time:.6f} seconds")