import timeit
def compare_types():
    int_val = 1000000000
    float_val = 999999999.5
    start_time = timeit.default_timer()
    for _ in range(1_000_000):
        if int_val == float_val:
            pass
    end_time = timeit.default_timer()
    return end_time - start_time
if __name__ == '__main__':
    elapsed_seconds = compare_types()
    print(f"Execution time for 1,000,000 comparisons: {elapsed_seconds:.4f} seconds")