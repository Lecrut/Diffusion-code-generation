import timeit
def count_elements_optimized(data):
    return len(data)
if __name__ == '__main__':
    large_dataset = list(range(10_000_000))
    start_time = timeit.default_timer()
    result_count = count_elements_optimized(large_dataset)
    end_time = timeit.default_timer()
    print(f"Total elements: {result_count}")
    print(f"Execution time (seconds): {end_time - start_time:.6f}")