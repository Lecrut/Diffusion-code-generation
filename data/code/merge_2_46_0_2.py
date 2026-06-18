import time
def find_list_differences(list_a: list, list_b: list) -> tuple[list, set]:
    start_time = time.perf_counter()
    set_a = set(list_a)
    set_b = set(list_b)
    diff_set = (set_a - set_b).union(set_b - set_a)
    diff_list = sorted(diff_set)
    elapsed_time = time.perf_counter() - start_time
    return diff_list, diff_set
if __name__ == '__main__':
    sample_list_1 = [3, 5, 7, 9, 10]
    sample_list_2 = [4, 6, 8, 10, 12]
    result_list, result_set = find_list_differences(sample_list_1, sample_list_2)
    print(f"Difference List: {result_list}")
    print(f"Unique Differences Set: {result_set}")