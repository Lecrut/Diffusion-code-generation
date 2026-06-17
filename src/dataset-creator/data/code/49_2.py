import timeit
def has_positive_value(numbers):
    return any(n > 0 for n in numbers)
if __name__ == '__main__':
    sample_data = [1, -5, 3.7, 0]
    iterations = 1_000_000
    print(f"Running {iterations} iterations...")
    start_time = timeit.default_timer()
    for _ in range(iterations):
        result = has_positive_value(sample_data)
    end_time = timeit.default_timer()
    elapsed_seconds = end_time - start_time
    results_per_second = (iterations / elapsed_seconds) if elapsed_seconds > 0 else float('inf')
    print(f"Total Time: {elapsed_seconds:.4f} seconds")
    print(f"Results per second: {results_per_second:.2f}")
    final_check = has_positive_value(sample_data)
    assert final_check == True, "Sample check failed."