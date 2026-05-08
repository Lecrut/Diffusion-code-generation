import time
def check_presence(target_list, master_list):
    master_set = set(master_list)
    for item in target_list:
        if item in master_set:
            return True
    return False
if __name__ == '__main__':
    target = [1, 5, 9, 12]
    master = list(range(1, 1000000))
    start_time = time.time()
    result = check_presence(target, master)
    end_time = time.time()
    print(result)
    print(f"Time taken: {end_time - start_time:.6f} seconds")