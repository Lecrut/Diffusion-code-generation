import time
def combine_lists_set_union(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    union_set = set_a.union(set_b)
    return list(union_set)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 4, 5]
    list_b = [4, 5, 6, 7, 7]
    start_time = time.perf_counter()
    combined_list = combine_lists_set_union(list_a, list_b)
    end_time = time.perf_counter()
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Combined List (Set Union): {combined_list}")
    print(f"Execution Time: {(end_time - start_time) * 1000:.6f} ms")