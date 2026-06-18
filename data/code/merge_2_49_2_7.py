import timeit
def has_positive_value(numbers):
    return any(n > 0 for n in numbers)
if __name__ == '__main__':
    sample_data = [1, -5, 3.7, 0, -2]
    iterations = 1_000_000
    print(f"Running {iterations} iterations...")
    start_time = timeit.default_timer()
    for _ in range(iterations):
        result = has_positive_value(sample_data)
    end_time = timeit.default_timer()
    elapsed_seconds = end_time - start_time
    average_per_call_ms = (elapsed_seconds / iterations) * 1000
    print(f"Total Time: {elapsed_seconds:.4f} seconds")
    print(f"Avg per call: {average_per_call_ms:.6f} ms")
    expected_result = True
    actual_result = has_positive_value(sample_data)
    if actual_result == expected_result:
        print("Verification passed.")
    else:
        print("Verification failed.")