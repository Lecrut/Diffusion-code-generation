import timeit
def check_positive(numbers):
    return any(n > 0 for n in numbers)
if __name__ == '__main__':
    sample_data = [1, -5, 3.7, 0, 2]
    iterations = 1_000_000
    print(f"Running {iterations} checks...")
    start_time = timeit.default_timer()
    for _ in range(iterations):
        result = check_positive(sample_data)
    end_time = timeit.default_timer()
    elapsed_seconds = end_time - start_time
    results_per_second = iterations / elapsed_seconds
    print(f"Total checks: {iterations}")
    print(f"Time taken: {elapsed_seconds:.4f} seconds")
    print(f"Checks per second: {results_per_second:.2f}")
    test_cases = [
        [-1, -2],                        
        [0, 0],                       
        [5, 3.14],                          
        [],                            
    ]
    print("\nSample verification results:")
    for data in test_cases:
        is_positive = check_positive(data)
        print(f"Data {data}: {'Positive value exists' if is_positive else 'No positive value'}")