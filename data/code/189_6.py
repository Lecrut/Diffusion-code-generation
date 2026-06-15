my_list = [1, 2, 3, 4, 5]
list_to_modify = [1, 2, 3, 4, 5]
print("--- Demonstration of .remove() ---")
list_for_remove = list_to_modify[:]
print(f"Original list before removal: {list_for_remove}")
item_to_remove_remove = 3
try:
    list_for_remove.remove(item_to_remove_remove)
    print(f"After .remove({item_to_remove_remove}): {list_for_remove}")
except ValueError as e:
    print(f"Error during .remove(): {e}")
print("\n--- Demonstration of del keyword ---")
list_for_del = list_to_modify[:]
print(f"Original list before deletion: {list_for_del}")
item_to_delete_del = 2
del list_for_del[1]
print(f"After del list_for_del[1]: {list_for_del}")
print("\n--- Performance and Immutability Comparison ---")
list_perf_remove = [10, 20, 30, 40, 50]
item_remove_val = 30
import time
start_time = time.perf_counter()
list_perf_remove.remove(item_remove_val)
end_time = time.perf_counter()
print(f"Time taken for .remove({item_remove_val}): {end_time - start_time:.6f} seconds")
list_perf_del = [10, 20, 30, 40, 50]
index_del = 2
start_time = time.perf_counter()
del list_perf_del[index_del]
end_time = time.perf_counter()
print(f"Time taken for del list_perf_del[{index_del}]: {end_time - start_time:.6f} seconds")
list_to_compare = [10, 20, 30, 40, 50]
item_val = 30
index_of_item = list_to_compare.index(item_val)
start_time = time.perf_counter()
del list_to_compare[index_of_item]
end_time = time.perf_counter()
print(f"Time taken for del using index ({index_of_item}): {end_time - start_time:.6f} seconds")
if __name__ == '__main__':
    pass