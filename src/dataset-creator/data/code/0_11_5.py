import timeit
def compare_types():
    a = 100
    b = float('inf')
    result_a_b = (a == b)
    result_float_int = (b == a)
    return {
        'int_vs_inf': result_a_b,
        'inf_vs_int': result_float_int
    }
if __name__ == '__main__':
    iterations = 10_000_000
    setup_code = "a=1; b=float('inf'); c=a==b"
    elapsed_time = timeit.timeit(setup_code, number=iterations)
    print(f"Time taken for {iterations} comparisons: {elapsed_time:.4f}s")