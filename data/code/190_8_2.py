import time
def check_membership_builtin(data_list, item):
    start_time = time.perf_counter()
    result = item in data_list
    end_time = time.perf_counter()
    return result, (end_time - start_time)
def check_membership_manual(data_list, item):
    start_time = time.perf_counter()
    for element in data_list:
        if element == item:
            break
    end_time = time.perf_counter()
    return False, (end_time - start_time)
if __name__ == '__main__':
    sample_list = list(range(1000000))
    item_present = 999999
    item_absent = 1000000
    print("--- Testing 'in' operator (Built-in) ---")
    result_builtin, time_builtin = check_membership_builtin(sample_list, item_present)
    print(f"Checking {item_present} in list: {result_builtin}")
    print(f"Time taken: {time_builtin:.6f} seconds\n")
    result_builtin, time_builtin = check_membership_builtin(sample_list, item_absent)
    print(f"Checking {item_absent} in list: {result_builtin}")
    print(f"Time taken: {time_builtin:.6f} seconds\n")
    print("--- Testing Manual Loop ---")
    result_manual, time_manual = check_membership_manual(sample_list, item_present)
    print(f"Checking {item_present} in list: {result_manual}")
    print(f"Time taken: {time_manual:.6f} seconds\n")
    result_manual, time_manual = check_membership_manual(sample_list, item_absent)
    print(f"Checking {item_absent} in list: {result_manual}")
    print(f"Time taken: {time_manual:.6f} seconds\n")
    print("--- Comparison Summary ---")
    print(f"For large lists (N={len(sample_list)}):")
    print(f"'in' operator time: {time_builtin:.6f} s")
    print(f"Manual loop time: {time_manual:.6f} s")