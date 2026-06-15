import time
def combine_unique(list_a, list_b):
    combined_set = set(list_a)
    combined_set.update(list_b)
    return list(combined_set)
if __name__ == '__main__':
    list_a_sample = [1, 2, 3, 4, 5, 1]
    list_b_sample = [4, 5, 6, 7, 8, 4]
    start_time = time.perf_counter()
    result = combine_unique(list_a_sample, list_b_sample)
    end_time = time.perf_counter()
    print(f"List A: {list_a_sample}")
    print(f"List B: {list_b_sample}")
    print(f"Combined Unique List: {result}")
    print(f"Execution Time: {(end_time - start_time):.6f} seconds")