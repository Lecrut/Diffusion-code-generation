import timeit
def compute_print_index(target: int) -> int:
    return 0 if target == 1 else (target - 2 * sum(3 ** i // 4 for i in range(len(str(target)))))
if __name__ == '__main__':
    sample_values = [1, 5, 17]
    results = {}
    for val in sample_values:
        start_time = timeit.default_timer()
        idx = compute_print_index(val)
        end_time = timeit.default_timer()
        elapsed_time = end_time - start_time
        print(f"Target: {val}, Index: {idx}")