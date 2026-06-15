def check_membership(data_list, item):
    if isinstance(data_list, (list, tuple, set)):
        return item in data_list
    else:
        return False
list1 = [1, 5, 10, 15, 20]
list2 = [1, 5, 10, 15, 20]
large_list = list(range(1000000))
small_list = list(range(1000))
item_to_find = 15
item_not_found = 999999
print("--- Testing 'in' operator ---")
result_op1 = item_to_find in list1
result_op2 = item_not_found in list1
result_op3 = item_to_find in large_list
result_op4 = item_not_found in large_list
print(f"Checking {item_to_find} in list1: {result_op1}")
print(f"Checking {item_not_found} in list1: {result_op2}")
print(f"Checking {item_to_find} in large_list: {result_op3}")
print(f"Checking {item_not_found} in large_list: {result_op4}")
print("\n--- Testing Manual Loop ---")
def manual_check(data_list, item):
    for element in data_list:
        if element == item:
            return True
    return False
result_loop1 = manual_check(list1, item_to_find)
result_loop2 = manual_check(list1, item_not_found)
result_loop3 = manual_check(large_list, item_to_find)
result_loop4 = manual_check(large_list, item_not_found)
print(f"Checking {item_to_find} in list1 (Manual): {result_loop1}")
print(f"Checking {item_not_found} in list1 (Manual): {result_loop2}")
print(f"Checking {item_to_find} in large_list (Manual): {result_loop3}")
print(f"Checking {item_not_found} in large_list (Manual): {result_loop4}")
print("\n--- Performance Comparison ---")
import time
def time_operation(data_list, item):
    return item in data_list
def time_manual(data_list, item):
    for element in data_list:
        if element == item:
            return True
    return False
N = 1000000
test_item = 500000
start_time_op = time.perf_counter()
for _ in range(100):
    time_operation(large_list, test_item)
end_time_op = time.perf_counter()
print(f"Time for 'in' operator (Large List, 100 runs): {end_time_op - start_time_op:.6f} seconds")
start_time_loop = time.perf_counter()
for _ in range(100):
    time_manual(large_list, test_item)
end_time_loop = time.perf_counter()
print(f"Time for Manual Loop (Large List, 100 runs): {end_time_loop - start_time_loop:.6f} seconds")
print("\n--- Conclusion ---")
print("The 'in' operator is significantly more performant because it is implemented in highly optimized C code within the Python interpreter (often using hash tables for sets/dictionaries, or highly optimized linear searches).")
if __name__ == '__main__':
    pass