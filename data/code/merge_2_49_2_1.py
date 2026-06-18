import timeit
def has_positive_value(numbers):
    return any(n > 0 for n in numbers)
if __name__ == '__main__':
    test_data = [1, -5, 3.7, 0]
    iterations = 1_000_000
    print(f"Running {iterations} iterations...")
    start_time = timeit.default_timer()
    result_set = set()
    for _ in range(iterations):
        if has_positive_value(test_data):
            result_set.add(True)
    end_time = timeit.default_timer()
    elapsed_seconds = end_time - start_time
    print(f"Total Time: {elapsed_seconds:.4f} seconds")
    print(f"Average per call: {(elapsed_seconds / iterations * 1_000_000):.6f} microseconds")
    print(f"All checks passed consistently: {len(result_set) == 1}")