import timeit
def has_positive_value(numbers):
    return any(n > 0 for n in numbers)
if __name__ == '__main__':
    test_data = [1, -2, 3.5]
    iterations = 1_000_000
    print(f"Running {iterations} iterations...")
    start_time = timeit.default_timer()
    result_set = set()
    for _ in range(iterations):
        if has_positive_value(test_data):
            result_set.add(True)
    end_time = timeit.default_timer()
    elapsed_seconds = end_time - start_time
    print(f"Result: {result_set}")
    print(f"Time taken: {elapsed_seconds:.4f} seconds")