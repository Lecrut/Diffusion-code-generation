import timeit
def compare_types():
    a = 100
    b = float('inf')
    result_a = (a == b)
    result_b = (float(a) == b)
    return {
        'int_vs_float_direct': result_a,
        'casted_comparison': result_b
    }
if __name__ == '__main__':
    iterations = 10_000_000
    setup_code = "a=1; b=float('inf'); c=a==b"
    elapsed_time = timeit.timeit(setup_code, number=iterations)
    print(f"Time taken for {iterations} comparisons: {elapsed_time:.4f}s")